import cv2, numpy as np
img=cv2.imread("input.jpg"); assert img is not None
h,w=img.shape[:2]; src=np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]]); dst=np.float32([[40,30],[w-80,0],[w-1,h-60],[20,h-1]]); H=cv2.getPerspectiveTransform(src,dst); out=cv2.warpPerspective(img,H,(w,h)); cv2.imwrite("output_warp.png",out)
