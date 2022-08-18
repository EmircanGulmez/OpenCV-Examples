import cv2

img = cv2.imread("contour.png") # Resmi çağırır

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Resmi grileştirir

ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # Görüntüyü ikilik görüntüye (binary) çevirir

M = cv2.moments(thresh) # Sözlük içerisinde bazı parametreler tutar
print(M)

# Bazı parametreler içerisinde işlem yaparak koordinatlar çıkarılır
x = int(M["m10"] / M["m00"])
y = int(M["m01"] / M["m00"])

cv2.circle(img, (x,y), 5, (0,0,0), -1) # Daire çizme (resim değişkeni, merkez nok. koordinatlar, yarı çap, BGR renk, kalınlık)

cv2.imshow("img",img) # Resmi ekranda gösterme

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
