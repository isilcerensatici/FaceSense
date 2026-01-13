import cv2
import mediapipe as mp
import pandas as pd
from datetime import datetime
import math

# MediaPipe Face Mesh modelini başlat / Initialize MediaPipe Face Mesh model
# 0.5 güven değeri modelin hassasiyetini belirler / 0.5 confidence value sets detection sensitivity
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Kamera bağlantısı / Video capture connection
cap = cv2.VideoCapture(0)
data = []

print("Kamera açıldı. Çıkmak için 'q' basınız. / Camera started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntü işleme: Aynalama ve Renk Dönüşümü / Preprocessing: Mirroring and Color Conversion
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # MediaPipe uses RGB, OpenCV uses BGR
    results = face_mesh.process(rgb_frame) # Yüz tespiti / Process face landmarks
    
    h, w, _ = frame.shape
    ifade = "Notr"

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Dudak koordinatlarını al / Get lip coordinates
            # MediaPipe uses specific indices for landmarks (e.g., 13, 14, 61, 291 for lips)
            ust_dudak = face_landmarks.landmark[13]
            alt_dudak = face_landmarks.landmark[14]
            sol_kenar = face_landmarks.landmark[61]
            sag_kenar = face_landmarks.landmark[291]

            # Koordinatları piksele çevir / Convert normalized coordinates to pixels
            cx_ust, cy_ust = int(ust_dudak.x * w), int(ust_dudak.y * h)
            cx_alt, cy_alt = int(alt_dudak.x * w), int(alt_dudak.y * h)
            cx_sol, cy_sol = int(sol_kenar.x * w), int(sol_kenar.y * h)
            cx_sag, cy_sag = int(sag_kenar.x * w), int(sag_kenar.y * h)

            # --- MANTIK HESAPLAMALARI / LOGICAL CALCULATIONS ---
            
            # 1. Ağız Açıklığı / Mouth Opening (For Surprise)
            agiz_acikligi = cy_alt - cy_ust
            
            # 2. Gülümseme-Üzülme Eğrisi / Smile-Sadness Curvature
            # Kenarların merkezi ile dudak merkezini kıyasla / Compare mouth corners to mouth center
            kenarlar_y_ort = (cy_sol + cy_sag) / 2
            merkez_y_ort = (cy_ust + cy_alt) / 2
            egrilik = merkez_y_ort - kenarlar_y_ort

            # --- KARAR MEKANİZMASI / DECISION LOGIC ---
            if agiz_acikligi > 25: 
                ifade = "Saskin" # Surprised
            elif egrilik > 4:      
                ifade = "Mutlu"  # Happy
            elif egrilik < -4:     
                ifade = "Uzgun"  # Sad
            else:
                ifade = "Notr"   # Neutral

            # --- GÖRSELLEŞTİRME / VISUALIZATION ---
            # Yüz çerçevesi / Face bounding box
            yuz_x_min = int(min([l.x for l in face_landmarks.landmark]) * w)
            yuz_y_min = int(min([l.y for l in face_landmarks.landmark]) * h)
            yuz_x_max = int(max([l.x for l in face_landmarks.landmark]) * w)
            yuz_y_max = int(max([l.y for l in face_landmarks.landmark]) * h)
            cv2.rectangle(frame, (yuz_x_min, yuz_y_min), (yuz_x_max, yuz_y_max), (255, 0, 0), 2)

            # Dudak takibi / Lip tracking visuals
            cv2.rectangle(frame, (cx_sol-10, cy_ust-10), (cx_sag+10, cy_alt+10), (0, 255, 0), 1)
            cv2.circle(frame, (cx_sol, cy_sol), 2, (0,0,255), -1)
            cv2.circle(frame, (cx_sag, cy_sag), 2, (0,0,255), -1)

            # Sonucu yazdır / Put emotion text
            cv2.putText(frame, f"Ifade: {ifade}", (yuz_x_min, yuz_y_min - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            # Veri kaydı / Log data
            data.append({
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Emotion": ifade,
                "Aperture": agiz_acikligi,
                "Curvature": egrilik
            })

    cv2.imshow("Geometric Emotion Analysis", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Excel Kaydı / Save to Excel
if data:
    df = pd.DataFrame(data)
    df.to_excel("geometric_analysis.xlsx", index=False)
    print("Excel dosyası kaydedildi. / Excel file saved.")