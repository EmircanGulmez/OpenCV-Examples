import cv2

img = cv2.imread("klon.jpg") # Resmi okur ve dizine dönüştürürüp img değişkenine atar.
print("Boyut (y,x):", img.shape[:2]) # Resmin boyutu

roi = img[30:200, 200:370] # [y ekseni başlangıç : bitiş, x ekseni başlangıç : bitiş]

cv2.imshow("Asker", img) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.
cv2.imshow("ROI", roi) # Pencerede kesilem resmi gösterir ve pencerenin sol üste metin yazar.

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.