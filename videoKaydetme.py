""" Kameradan açılan görüntüyü kaydetme """

import cv2 # OpenCV kütüphanesi tanımlama

cap = cv2.VideoCapture(0) # Kamera açma

fileName = "webcam.avi" # Dosyanın kayıt olacağı konumu ve isimle uzantısı
codec = cv2.VideoWriter_fourcc('W','M','V','2') # Media verilerinde codecleri tanımlar
frameRate = 30 # Saniyelik görüntü sayısı
resolution = (640, 480) # Çözünürlük
videoFile = cv2.VideoWriter(fileName, codec, frameRate, resolution) # Okunan frameleri dosya içerisine video şeklinde kaydı

while True:
    # ret -> cap değişkenin doğru okuyup okumadığını yazar (true, false)
    # frame -> okunan kareleri (frameleri) yazar
    ret, frame = cap.read() # cap.read() 2 adet değer okur
    frame = cv2.flip(frame, 1) # Her bir görüntüyü eksenlerde yansıtmaya yarar.
    # (1 -> y ekseni / 0 -> x ekseni / -1 -> orjine göre)
    videoFile.write(frame) # Frameleri videoFile değişkenine yazar.
    cv2.imshow("PC Kamera", frame) # Alınan frameler ekranda gösterilir

    # 0xFF == ord("q") -> Klavyeden girilen karaktere göre işlem yapar.
    if cv2.waitKey(25) & 0xFF == ord("q"): # 25 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

videoFile.release() # Kaydı durdurur.
cap.release() # cap değişkenini okutmayı bırakır
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.