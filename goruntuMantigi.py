import cv2
import numpy as np

img = np.zeros((10,10,3), np.uint8) # 3 kanallı 10x10 luk

img[0,0] = (255,255,255) # 0,0 noktasındaki pikselin rengi
img[0,1] = (255,255,200) # 0,1 noktasındaki pikselin rengi
img[0,2] = (255,255,150) # 0,2 noktasındaki pikselin rengi
img[0,3] = (255,255,15) # 0,3 noktasındaki pikselin rengi
"""
img = np.zeros((10,10), np.uint8) # tek kanallı 10x10 luk

img[0,0] = 255 # 0,0 noktasındaki pikselin gri tonlarındaki rengi
img[0,1] = 200 # 0,1 noktasındaki pikselin gri tonlarındaki rengi
img[0,2] = 100 # 0,2 noktasındaki pikselin gri tonlarındaki rengi
img[0,3] = 15 # 0,3 noktasındaki pikselin gri tonlarındaki rengi
"""
img = cv2.resize(img, (1000,1000), interpolation = cv2.INTER_AREA) # pikselleri 100 kat büyütüyoruz.

cv2.imshow("Canvas", img) # Pencerede olşturulan tuval gösterilir
cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.
