import cv2
import numpy as np

img = cv2.imread("klon.jpg",0)

kernel = np.ones((5,5), np.uint8) # Birlerden oluşan matrixler

# (resim değişkeni, matrix dizesi, tekrarlama)
erosion = cv2.erode(img, kernel, iterations = 1) # Siyahlar artıyor
dilation = cv2.dilate(img, kernel, iterations = 1) # Beyazlıklar artıyor
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # Resimde ki gürültüyü kaldırır
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # Nesnenin uyumsuzlukları siler
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) # Nesnenin dış kısımları beyaz çizer diğer kısımlar siyah
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) # Nesnenin bazı kısımları beyaz diğer kısımları siyah olur

cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradient", gradient)
cv2.imshow("tophat", tophat)

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
