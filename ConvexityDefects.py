import cv2
import numpy as np

img = cv2.imread("star.png") # Resmi çağırır

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Resmi gri formata dönüştürür
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # Görüntüyü ikilik görüntüye (binary) çevirir

# (thresh değişkeni, hata azaltmak için varsayılan argümanlar)
contours, hierarchy = cv2.findContours(thresh,2,1) # kontur koordinatlarını bulur

cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints = False) # contours 0. index değerleri ile dış örtü oluşturur,
# returnPoints = False olması indekslerin kendileri değil değerlirinin dönmesidir.

defects = cv2.convexityDefects(cnt,hull) # Kusurları arar

for i in range(defects.shape[0]): # defectsin 0. elemanı kadar döner
    s, e, f, d = defects[i,0] # s -> start point (yıldızın dış uç noktaları), e -> end point, f -> furthest point, d -> distance

    start = tuple(cnt[s][0]) # başlangıç noktası
    end = tuple(cnt[e][0]) # bitiş noktası
    far = tuple(cnt[f][0]) # en uzak nokta

    cv2.line(img,start,end,[0,255,0],2) # dış bükey örtü çizgi çizme
    cv2.circle(img,far,5,[0,255,0],-1) # içe bükülmüş noktalara daire çizme

cv2.imshow("img",img) # Resimleri ekranda gösterme

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
