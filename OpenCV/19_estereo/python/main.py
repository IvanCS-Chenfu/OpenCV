import cv2, numpy as np
L=cv2.imread("left.png",0); R=cv2.imread("right.png",0); assert L is not None and R is not None
st=cv2.StereoSGBM_create(minDisparity=0,numDisparities=16*8,blockSize=5,P1=8*5*5,P2=32*5*5,uniquenessRatio=10,speckleWindowSize=100,speckleRange=2); disp=st.compute(L,R).astype(np.float32)/16.0; np.save("disparity.npy",disp); print("disparidad válida",np.count_nonzero(disp>0))
