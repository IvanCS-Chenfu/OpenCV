import cv2
import numpy as np

img = np.zeros((360, 640, 3), dtype=np.uint8)
img[:, :320] = (255, 0, 0)      # BGR: azul
img[:, 320:] = (0, 180, 255)    # naranja
roi = img[80:280, 220:420]
cv2.rectangle(img, (220, 80), (420, 280), (255, 255, 255), 2)
print("shape=", img.shape, "dtype=", img.dtype, "ROI=", roi.shape)
cv2.imwrite("output_fundamentos.png", img)
