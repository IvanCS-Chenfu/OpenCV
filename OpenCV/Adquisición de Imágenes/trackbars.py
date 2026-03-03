import cv2 as cv

def callback():
    pass

def trackbar(im):
    x1 = (433, 300)
    x2 = (565, 319)
    
    nombre_ventana = "trackbars"
    limite_inferior = 0
    limite_superior = 255
    
    cv.namedWindow(nombre_ventana)
    cv.createTrackbar("B", nombre_ventana, limite_inferior, limite_superior, callback)
    cv.createTrackbar("G", nombre_ventana, limite_inferior, limite_superior, callback)
    cv.createTrackbar("R", nombre_ventana, limite_inferior, limite_superior, callback)

    while True:
        cv.imshow(nombre_ventana, im)
        
        b = cv.getTrackbarPos("B", nombre_ventana)
        g = cv.getTrackbarPos("G", nombre_ventana)
        r = cv.getTrackbarPos("R", nombre_ventana)
        
        cv.circle(im, x1, 20, (b,g,r), -1) 
        cv.circle(im, x2, 20, (b,g,r), -1)
        
        if cv.waitKey(1) == ord('q'):
            break



if __name__ == '__main__':
    im = cv.imread("Gato.png")
    
    trackbar(im)