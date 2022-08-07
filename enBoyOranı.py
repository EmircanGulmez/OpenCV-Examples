""" Girilen en veya boy değerine göre piksel hesaplaması yaparak resmi bozmadan yeniden boyutlandırma yapar. """

import cv2 # OpenCV kütüphanesi tanımlama

def resizeWithAspectRatio(img, en = None, boy = None, inter = cv2.INTER_AREA): # (resim, en, boy, inter varsayılan ayarlama)
    boyut = None
    (b,e) = img.shape[:2] # Resmin boyutlarını alır (boy, en)

    if en is None and boy is None: # En boy girilmeze resmin orjinalini döndürür
        return img

    if en is None: # en değerini vermez ise:
        r = boy / float(b) # İstenen boy değişkenini resmin boyuna bölünür. float -> hassas olması için
        boyut = (int(e*r), boy) # Yeni boyut alnıır (hesaplanan en, istenilen boy).

    else: # boy değerini vermez ise:
        r = en / float(e) # İstenen en değişkenini resmin enine bölünür. float -> hassas olması için
        boyut = (en, int(b*r)) # Yeni boyut alınır (istenilen en, hesaplanan boy).

    return cv2.resize(img, boyut, interpolation = inter) # Yeni boyutlandırmayı geri döndürür.

img = cv2.imread("klon.jpg") # Resmi okur ve dizine dönüştürürüp img değişkenine atar.
img1 = resizeWithAspectRatio(img, en = None, boy = 600, inter = cv2.INTER_AREA) # Fonksiyona hesaplatılacak değerler gönderilir.

cv2.imshow("Orjinal", img) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.
cv2.imshow("Yeniden Boyutlandirilma", img1) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.