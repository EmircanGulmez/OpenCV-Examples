import cv2
import numpy as np

# Daire
# np.uint8 -> Çizim yaptığımız veri tipidir.
canvasCircle = np.zeros((512,512,3), dtype=np.uint8) + 255 # Siyah tuvali 255 ekleyerek beyaz haline getiriyoruz
cv2.circle(canvasCircle, (256,256), 60, (255,0,0), -1) # (tuval değişkeni, merkez nok, yarı çap, BGR rengi, kalınlık)

# Kare
canvasRectangle = np.zeros((512,512,3), dtype=np.uint8) + 255 # Siyah tuvali 255 ekleyerek beyaz haline getiriyoruz
cv2.rectangle(canvasRectangle, (150,150), (350,350), (0,0,255), -1) # (tuval değişken, sol üst nok, sağ alt nok, BGR rengi, kalınlık)

# kalınlık -1 olması şeklin içi dolmasıdır
# thickness yazmak zorunlu değil sadece kalınlık değeride yazılabilir.

# Normal BGR Toplam
add = cv2.add(canvasCircle,canvasRectangle) # Resimleri toplar
print(add[256,256])

# Ağırlıklı Toplam
dst = cv2.addWeighted(canvasCircle, 0.2, canvasRectangle, 0.8, 0)
# (resim1, resim1 oranı, resim2, resim2 oranı, sabit sayı) resim oranların toplamı 1 olmak zorundadır

cv2.imshow("Daire", canvasCircle) # Pencerede olşturulan tuval gösterilir
cv2.imshow("Kare", canvasRectangle) # Pencerede olşturulan tuval gösterilir
cv2.imshow("BGR Toplam", add) # Pencerede olşturulan tuval gösterilir
cv2.imshow("Agirlikli Toplam", dst) # Pencerede olşturulan tuval gösterilir

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.