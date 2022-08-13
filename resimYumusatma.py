import cv2

# Resimleri ekleme
imgFilter = cv2.imread("filter.png")
imgMedian = cv2.imread("median.png")
imgBilateral = cv2.imread("bilateral.png")

# Yumuşama değerleri pozitif tek sayı olmak zorundadır
blur = cv2.blur(imgFilter, (5,5)) # (resim değişkeni, yumuşama değeri)
blurG = cv2.GaussianBlur(imgFilter, (5,5), cv2.BORDER_DEFAULT) # (resim değişkeni, yumuşama değeri, sınır çizgileri varsayılan)
blurM = cv2.medianBlur(imgMedian, 5) # (resim değişkeni, yumuşama değeri)
blurB = cv2.bilateralFilter(imgBilateral, 9, 95, 95) # (resim değişkeni, piksel dönüşlüm değerleri)

# Resimleri ekranda gösterme
cv2.imshow("Orjinal Filter", imgFilter)
cv2.imshow("Orjinal Median", imgMedian)
cv2.imshow("Orjinal Bilateral", imgBilateral)

cv2.imshow("blur", blur)
cv2.imshow("blurG", blurG)
cv2.imshow("blurM", blurM)
cv2.imshow("blurB", blurB)

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
