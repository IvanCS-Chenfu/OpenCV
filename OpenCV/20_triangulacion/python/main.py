import cv2, numpy as np
P1=np.loadtxt("P1.txt"); P2=np.loadtxt("P2.txt"); x1=np.loadtxt("points1.txt").T; x2=np.loadtxt("points2.txt").T; Xh=cv2.triangulatePoints(P1,P2,x1,x2); X=(Xh[:3]/Xh[3]).T; np.savetxt("points3d.txt",X); print(X[:5])
