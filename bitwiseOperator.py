import cv2

# Resimleri ekleme
img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

# Resimlerin bit düzeyinde karşılaştırma yapılacak
bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img2, img1)

# Resimlerin bit düzeyinde tersini alacak
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

# Resimleri ekranda gösterme
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not1",bit_not)
cv2.imshow("bit_not2",bit_not2)

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
