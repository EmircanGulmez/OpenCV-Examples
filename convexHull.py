import cv2
import numpy as np

img = cv2.imread("map.jpg") # Resmi çağırır

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Resmi gri formata dönüştürür
blur = cv2.blur(gray,(3,3)) # Resmi yumuşatma

ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY) # Görüntüyü ikilik görüntüye (binary) çevirir

# (thresh değişkeni, hata azaltmak için varsayılan argümanlar)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # kontur koordinatlarını bulur

hull = [] # convex hull noktalarını atamak için boş dizi

for i in range(len(contours)): # her değeri görmek için döngü oluşturulur
    hull.append(cv2.convexHull(contours[i],False)) # False olduğu için contoursun her indisindeki değeri döndürülür

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8) # 0 lardan oluşan siyah ekran oluşturulur

# (resim değişkeni, koordinatlar, bölge, renkler, kalınlık)
# bölge -> -1 ise cizim + penzere kenarları, 0 ise sadece pencere kenarları, 1 ise sadece cisim kenarlarını çizer
for i in range(len(contours)): # hierarchy yazmak zorunlu değil (bazı konturları çizmek için kullanılır)
   cv2.drawContours(bg,contours,i,(255,0,0),3,8,hierarchy) # Haritanın kendi dış çizgileri
   cv2.drawContours(bg,hull,i,(0,255,0),1,8) # ConvexHull (dış bükey örtü)

# Resimleri ekranda gösterme
cv2.imshow("orjinal",img)
cv2.imshow("image",bg)

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.