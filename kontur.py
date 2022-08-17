import cv2

img = cv2.imread('contour1.png') # Resmi çağırır
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Resmi grileştirir

# (resim değişkeni, esik değeri, max threshold değeri, threshold tipi)
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # Görüntüyü ikilik görüntüye (binary) çevirir

# (thresh değişkeni, hata azaltmak için varsayılan argümanlar)
contours,ret = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # kontur koordinatlarını bulur

# (resim değişkeni, koordinatlar, bölge, renkler, kalınlık)
# bölge -> -1 ise cizim + penzere kenarları, 0 ise sadece pencere kenarları, 1 ise sadece cisim kenarlarını çizer
cv2.drawContours(img, contours, 1, (0,0,255), 3) # bulunan koordinatları birleştirir çizer

cv2.imshow("contour",img) # Resmi ekranda gösterir

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.