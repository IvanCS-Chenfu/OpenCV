import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened(): raise RuntimeError("No se pudo abrir la cámara")
while True:
    ok, frame = cap.read()
    if not ok: break
    cv2.imshow("camara", frame)
    if cv2.waitKey(1) & 0xFF in (27, ord('q')): break
cap.release(); cv2.destroyAllWindows()
