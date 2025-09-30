import cv2

im = cv2.imread('Figuras.png')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_canny = cv2.Canny(im_gray, 10, 150)

# Para que se junte el contorno del triángulo
im_canny = cv2.dilate(im_canny, None, iterations=1)
im_canny = cv2.erode(im_canny, None, iterations=1)

cnts,_ = cv2.findContours(im_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    # Ambos "True" son debido a que las curvas son cerradas. En el caso contrario: False.
	epsilon = 0.01*cv2.arcLength(c,True)            # Parámetro que sirve para la precisión de la aproximación siguiente.
	approx = cv2.approxPolyDP(c,epsilon,True)       # Aproxima un contorno a un polígono. La longitud de "approx" es el número de vértices
 
	x,y,w,h = cv2.boundingRect(approx)

	if len(approx)==3:
		cv2.putText(im,'Triangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio == 1:
			cv2.putText(im,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
		else:
			cv2.putText(im,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(im,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==6:
		cv2.putText(im,'Hexagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>10:
		cv2.putText(im,'Circulo', (x,y-5),1,1,(0,255,0),1)

	cv2.drawContours(im, [approx], 0, (0,255,0),2)
	cv2.imshow('image',im)
	cv2.waitKey(0)