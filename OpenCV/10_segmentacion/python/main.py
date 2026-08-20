import cv2
g=cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE); assert g is not None
_,otsu=cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU); adap=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,5); cv2.imwrite("output_otsu.png",otsu); cv2.imwrite("output_adaptive.png",adap)
