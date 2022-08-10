import cv2

img = cv2.imread("klon.jpg") # Resmi okur ve dizine dönüştürürüp img değişkenine atar.

dimension = img.shape
print("Boyut:", dimension)

# Koordinata göre BGR değerlerini öğrenme
color = img[420, 500]
print("BGR:", color)

blue = img[420, 500, 0]
print("Mavi:", blue)

green = img[420, 500, 1]
print("Yesil:", green)

red = img[420, 500, 2]
print("Kırmızı:", red)

# Koordinata göre BGR değerlerini değiştirme
img[420, 500, 0] = 250
print("Yeni Mavi:", img[420, 500, 0])

# Fonksiyonlarla koordinata göre BGR değeri değiştirme
blue2 = img.item(150,200,0) # Mavi değerinin koordinatını hafızada tutma
print("Mavi2:", blue2)
img.itemset((150,200,0), 172) # Koordinatlara göre mavi değerini değiştirir
print("Yeni Mavi2:", img[150, 200, 0]) # Değiştirilen koordinatlar BGR değeri yazdırılır

cv2.imshow("Asker", img) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.
cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
