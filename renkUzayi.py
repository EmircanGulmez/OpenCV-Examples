import cv2  # OpenCV kütüphanesi tanımlama

# Resimlerde renk uzayı
img = cv2.imread("klon.jpg") # Resmi okur ve dizine dönüştürürüp img değişkenine atar.

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR dan RGB dönüştürme
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # BGR dan HSV dönüştürme
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR dan GRAY dönüştürme

cv2.imshow("Asker BGR", img) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.
cv2.imshow("Asker RGB", img_rgb) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.
cv2.imshow("Asker HSV", img_hsv) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.
cv2.imshow("Asker GRAY", img_gray) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.

"""

cap = cv2.VideoCapture("antalya.mp4") # Video açma

while True:
    # ret -> cap değişkenin doğru okuyup okumadığını yazar (true, false)
    # frame -> okunan kareleri (frameleri) yazar
    ret, frame = cap.read() # cap.read() 2 adet değer okur
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("PC Kamera", frame) # Alınan frameler ekranda gösterilir

    if ret == 0: # frame okuyamadığı için ret 0 olur ve videoyu okuyamaz döngüden çıkış yapar
        break

    # 0xFF == ord("q") -> Klavyeden girilen karaktere göre işlem yapar.
    if cv2.waitKey(25) & 0xFF == ord("q"): # 25 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

cap.release() # cap değişkenini okutmayı bırakır
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
"""