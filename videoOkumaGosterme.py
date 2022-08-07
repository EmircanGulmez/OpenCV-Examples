""" Bilgisayar kamerasından görüntü açma ve kapatma ile bilgisayardaki videoyu oynatma """

import cv2 # OpenCV kütüphanesi tanımlama

"""
0 -> PC'nin sabit kamerasını kullanır
1 -> USB'ye bağlı olan kamerayı kullanır
"""
# cap = cv2.VideoCapture(0) # Kamera açma
cap = cv2.VideoCapture("antalya.mp4") # Video açma

while True:
    # ret -> cap değişkenin doğru okuyup okumadığını yazar (true, false)
    # frame -> okunan kareleri (frameleri) yazar
    ret, frame = cap.read() # cap.read() 2 adet değer okur
    frame = cv2.flip(frame, 1) # Her bir görüntüyü eksenlerde yansıtmaya yarar.
    # (1 -> y ekseni / 0 -> x ekseni / -1 -> orjine göre)
    cv2.imshow("PC Kamera", frame) # Alınan frameler ekranda gösterilir

    if ret == 0: # frame okuyamadığı için ret 0 olur ve videoyu okuyamaz döngüden çıkış yapar
        break

    # 0xFF == ord("q") -> Klavyeden girilen karaktere göre işlem yapar.
    if cv2.waitKey(25) & 0xFF == ord("q"): # 25 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

cap.release() # cap değişkenini okutmayı bırakır
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.