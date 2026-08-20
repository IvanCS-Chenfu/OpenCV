import cv2
import matplotlib.pyplot as plt

imG = cv2.imread('Gente.png', 0)

hist = cv2.calcHist([imG],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()