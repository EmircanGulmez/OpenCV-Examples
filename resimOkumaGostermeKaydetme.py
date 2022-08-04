import cv2  # OpenCV kütüphanesi tanımlama

img = cv2.imread("klon.jpg") # Resmi okur ve dizine dönüştürürüp img değişkenine atar.
# img = cv2.imread("C:\Desktop\klon.jpg") # Resmi belli bir adresden okur ve dizine dönüştürürüp img değişkenine atar.
# img = cv2.imread("klon.jpg",0) # Resmi dizine dönüştürürken grileştirir.
# img = cv2.imread("klon.jpg", cv2.IMREAD_GRAYSCALE)  # Resmi dizine dönüştürürken grileştirir.
# print(img) # Terminalde resmin matrix değerlerini yazdırır.

cv2.namedWindow("image",cv2.WINDOW_NORMAL) # Yeni bir pencere açar ve resimle isimleri aynı olduğu için birleştirir.
img = cv2.resize(img,(640,580)) # cv2.namedWindow("image") şeklinde kullanarak resmi boyutlandır.
cv2.imshow("image", img) # Pencerede resmi gösterir ve pencerenin sol üste metin yazar.

cv2.imwrite("klon1.jpg",img) # Resmi dosyaya kayıt eder.
# cv2.imwrite("C:\Desktop\klon1.jpg",img) # Resmi belli bir adrese kayıt eder.

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
