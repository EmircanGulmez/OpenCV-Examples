import cv2
import numpy as np

# np.uint8 -> Çizim yaptığımız veri tipidir.
canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 # Siyah tuvali 255 ekleyerek beyaz haline getiriyoruz
print(canvas)

# thickness yazmak zorunlu değil sadece kalınlık değeride yazılabilir.

# Çizgi Çizme
# (tuval değişken, başlangıç nok, bitiş nok, BGR rengi, kalınlık)
cv2.line(canvas, (50,50), (400,400), (255,0,0), thickness = 5)

# Kare ve Dikdörtgen Çizme (İçi Boş veya Dolu "-1")
cv2.rectangle(canvas, (20,20), (150,200), (0,255,0), 2) # (tuval değişken, sol üst nok, sağ alt nok, BGR rengi, kalınlık)
cv2.rectangle(canvas, (150,230), (200,280), (0,0,255), thickness = -1) # kalınlık -1 olması şeklin içi dolmasıdır

# Çember ve Daire Çizme (İçi Boş veya Dolu "-1")
# (tuval değişkeni, merkez nok, yarı çap, BGR rengi, kalınlık)
cv2.circle(canvas, (150,400), 100, (0,0,255), thickness = 7)
cv2.circle(canvas, (400,100), 50, (0,255,255), -1) # kalınlık -1 olması şeklin içi dolmasıdır

# Üçgen Çizme
# Üçgen çizmek için belli bir fonk yok o yüzden çizgilerle yapılır
# Pointler
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

# Pointlere göre çizgiler
cv2.line(canvas, p1, p2, (0,0,0), 4)
cv2.line(canvas, p2, p3, (0,0,0), 4)
cv2.line(canvas, p3, p1, (0,0,0), 4)

# Elips
# (tuval değişkeni, merkez nok, (genislik,yükseklik), yatay eksendeki açısı, başlangıç derece, bitiş derece, BGR rengi, kalınlık)
cv2.ellipse(canvas, (400,400), (100,50), 0, 0, 360, (255,255,0),-1)

# Pointer ile diğer şekilleri çizme (Yamuk, Çokgenler vs.)
# np.int32 -> numpy veri tipi (uint8 olmamasının nedeni şuan bir çizim olmaması sadece koordinat tanımlama)
# ([[ponit1], [point2], [point3], [point4]], veri tipi)
points = np.array([[110,200], [330,200], [290,400], [100,450]], np.int32)
# (tuval değişkeni, [koordinatlar], çokgenin kapalı olup olmaması, BGR değeri, kalınlık)
cv2.polylines(canvas, [points], True, (0,150,150), 5)

# Yazı Yazdırma
# fontlar
font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# (tuval değişkeni, yazı, yazının sol alt noktası, font, kalınlık, BGR rengi, yazının tipi)
cv2.putText(canvas, "OpenCV", (5,100), font2, 4, (0,0,0), cv2.LINE_AA)

cv2.imshow("Canvas", canvas) # Pencerede olşturulan tuval gösterilir
cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.