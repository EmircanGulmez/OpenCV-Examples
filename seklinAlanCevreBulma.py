import cv2

img = cv2.imread("contour.png") # Resmi çağırır

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Resmi grileştirir

ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # Görüntüyü ikilik görüntüye (binary) çevirir

# (thresh değişkeni, hata azaltmak için varsayılan argümanlar)
contours,ret = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # kontur koordinatlarını bulur

cnt = contours[0]
print(cnt)

# Alan Hesaplama
M = cv2.moments(cnt) # Sözlük içerisinde bazı parametreler tutar
print("Alan:",M["m00"])

area = cv2.contourArea(cnt)
print("Alan:",area)

# Çevre Hesaplama
perimeter = cv2.arcLength(cnt,True)
print("Çevre:",perimeter)

cv2.imshow("img",img) # Resmi ekranda gösterme

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
