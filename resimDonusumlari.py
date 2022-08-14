import cv2
import numpy as np

img = cv2.imread('klon.jpg', 0) # Resmi dizine dönüştürürken grileştirir.

row, col = img.shape # Resmin satır ve sütun sayılarını alma

"""
# Resim Dönüşüm Dizeyi
# 1,0 -> x için değer girme
# 0,1 -> y için değer girme
M = np.float32([[1,0,50], [0,1,200]]) # ([[x ekseni, değeri], [y ekseni, değeri]])
dst = cv2.warpAffine(img, M, (row,col)) # (resim değişkeni, transformasyon matrixi, (satır, sütun))

# Resim döndürme
M = cv2.getRotationMatrix2D((col/4, row/2), 180, 1) # 2 Boyutlu olduğu (sütun, satır), derece, ölçek)
dst = cv2.warpAffine(img, M, (col,row)) # (resim değişkeni, transformasyon matrixi, (sütun, satır))

cv2.imshow("dst",dst) # Ekran da gösterme
"""

# Thresholding

# (resim değişkeni, esik değeri, max threshold değeri, threshold tipi)
ret, th1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# Eşik değeri, o alanın çevresindeki değerlerin ortalamasıyla hesaplanarak bulunur ve işlem uygulanır.
# (resim değişkeni, max threshold değeri, threshold fonk, threshold tipi, blok boyutu "2"'ye bölümünden kalan 1 olmalı", G sabiti)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

# Eşik değeri, o alanın çevresindeki değerlerin Gauss yöntemiyle ağırlıklı toplamlarının ortalaması hesaplanarak bulunur ve işlem uygulanır.
# (resim değişkeni, max threshold değeri, threshold fonk, threshold tipi, blok boyutu "2"'ye bölümünden kalan 1 olmalı", G sabiti)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

cv2.imshow("img th1", th1)
cv2.imshow("img th2", th2)
cv2.imshow("img th3", th3)

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.