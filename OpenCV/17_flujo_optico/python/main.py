import cv2
cap=cv2.VideoCapture("input.mp4"); ok,prev=cap.read(); assert ok
pg=cv2.cvtColor(prev,cv2.COLOR_BGR2GRAY); pts=cv2.goodFeaturesToTrack(pg,400,0.01,8)
while True:
 ok,frame=cap.read();
 if not ok: break
 g=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY); nxt,status,err=cv2.calcOpticalFlowPyrLK(pg,g,pts,None); pts=nxt[status.ravel()==1].reshape(-1,1,2); pg=g
 print("tracks",len(pts))
