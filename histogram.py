# Histogram -> Resmin değer noktalarının grafiğini verir.

import cv2
import numpy as np
from matplotlib import pyplot as plt # matplotlib içerisindeki pyplot'u çağırır ve ismi plt olur (grafik çizmeye yarar)
"""
# Tabla üzerinde gösterim
img = np.zeros((500,500),np.uint8) + 50
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)
"""
# Resim üzerinde gösterim
img = cv2.imread("smile.jpg")
b, g, r = cv2.split(img) # Resim değişkninin BGR değerlerini ayırır ve değişkelere atar

cv2.imshow("resim", img) # Resmi ekranda gösterme

# (tüm pikselleri tek bir satıra dökme komutu, kaç değer olduğu, değer aralığı)
# plt.hist(img.ravel(), 256, [0,256]) # Histogramı çizer
plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])

plt.show() # Histogramı ekranda gösterir

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.



