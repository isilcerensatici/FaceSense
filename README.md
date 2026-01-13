FaceSense
Real-Time Geometric Facial Emotion Analysis
FaceSense is a real-time facial expression analysis project that detects basic emotions (Happy, Sad, Surprised, Neutral) using image processing techniques. The project employs a rule-based approach grounded in geometric measurements on the face.
📌 About the Project
This project was developed during the 4th year Fall Semester for the Image Processing course.
It was prepared as part of a term assignment given by Dr. Yusuf Uzun.
The main goal of the project is to perform emotion analysis without relying on heavy AI models, instead using geometric data obtained from specific facial reference points.
🧪 Development Process
• 	In the initial stage, basic experiments were conducted using only OpenCV.
At this stage, the system could only distinguish between Happy and Neutral expressions.
• 	Later, the Haar Cascade method was tested, but it was limited to detecting only Happy and Neutral expressions.
• 	Deep learning-based solutions (e.g., TensorFlow) were considered, but deemed too heavy and unnecessary for the scope of this project.
• 	Finally, Google’s open-source MediaPipe library was discovered.
MediaPipe proved to be the most suitable solution thanks to its high accuracy in detecting face, hand, pose, and joint movements.
🧠 Methodology
• 	Detect 468 facial reference points using MediaPipe Face Mesh
• 	Calculate lip openness and lip curvature
• 	Classify emotions based on predefined threshold values
Results:
• 	Displayed in real-time on the screen
• 	Logged with timestamps into an Excel file
🛠 Technologies Used
• 	Python
• 	OpenCV
• 	MediaPipe
• 	Pandas
• 	NumPy
📊 Outputs
• 	Real-time visualization of face and expressions
• 	Expression logs saved in 
🎯 Conclusion
FaceSense demonstrates that emotion analysis can be achieved through a geometric, rule-based approach without heavy machine learning models. The project serves as a strong example for understanding fundamental principles in image processing and facial analysis.

FaceSense
Gerçek Zamanlı Geometrik Yüz İfade Analizi
FaceSense, gerçek zamanlı yüz ifadelerini analiz ederek temel duyguları (Mutlu, Üzgün, Şaşkın, Nötr) tespit eden bir görüntü işleme projesidir. Proje, yüz üzerindeki geometrik ölçümleri temel alan kural tabanlı bir yaklaşım kullanmaktadır.
📌 Proje Hakkında
Bu proje, 4. sınıf Güz Dönemi kapsamında, Görüntü İşleme dersi için geliştirilmiştir.
Çalışma, Dr. Öğr. Üyesi Yusuf Uzun tarafından verilen dönem ödevi kapsamında hazırlanmıştır.
Projenin amacı, ağır yapay zeka modellerine ihtiyaç duymadan, yüz üzerindeki belirli referans noktalarından elde edilen geometrik veriler ile duygu analizi yapabilmektir.
🧪 Geliştirme Süreci
• 	İlk aşamada yalnızca OpenCV kullanılarak temel denemeler yapılmıştır.
Bu aşamada sistem yalnızca Mutlu ve Nötr ifadeleri ayırt edebilmiştir.
• 	Daha sonra Haar Cascade yöntemi denenmiş, ancak bu yaklaşımda da ifade çeşitliliği sınırlı kalmıştır.
• 	Derin öğrenme tabanlı çözümler (örneğin TensorFlow) değerlendirilmiş; ancak proje kapsamı için ağır ve gereksiz bulunmuştur.
• 	Son aşamada Google tarafından geliştirilen açık kaynaklı MediaPipe kütüphanesi keşfedilmiştir.
MediaPipe; yüz, el, poz ve eklem hareketlerini yüksek doğrulukla tespit edebilmesi sayesinde bu proje için en uygun çözüm olmuştur.
🧠 Kullanılan Yöntem
• 	MediaPipe Face Mesh ile yüz üzerindeki 468 referans noktası tespit edilir
• 	Dudak açıklığı ve dudak eğriliği hesaplanır
• 	Önceden belirlenen eşik değerlerine göre duygu sınıflandırması yapılır
Sonuçlar:
• 	Gerçek zamanlı olarak ekranda gösterilir
• 	Zaman damgalı şekilde Excel dosyasına kaydedilir
🛠 Kullanılan Teknolojiler
• 	Python
• 	OpenCV
• 	MediaPipe
• 	Pandas
• 	NumPy
📊 Çıktılar
• 	Gerçek zamanlı yüz ve ifade görselleştirmesi
• 	 dosyası ile ifade kayıtları
🎯 Sonuç
FaceSense, ağır makine öğrenmesi modelleri kullanmadan, geometrik ve kural tabanlı bir yaklaşımla duygu analizi yapılabileceğini göstermektedir. Proje, görüntü işleme ve yüz analizi alanında temel prensipleri anlamak için güçlü bir örnek sunmaktadır.
