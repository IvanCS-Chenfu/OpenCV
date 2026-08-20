import cv2
g=cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE); assert g is not None
sift=cv2.SIFT_create(); kp,des=sift.detectAndCompute(g,None); out=cv2.drawKeypoints(g,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS); print(len(kp),des.shape if des is not None else None); cv2.imwrite("output_sift.png",out)
