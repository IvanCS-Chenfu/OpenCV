import cv2
g=cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE); assert g is not None
corners=cv2.goodFeaturesToTrack(g,300,0.01,8,useHarrisDetector=True,k=0.04); print("esquinas",0 if corners is None else len(corners))
