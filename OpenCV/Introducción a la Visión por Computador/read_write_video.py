import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readVideo(videoPath):
    # Obtiene el objeto del video (ya sea grabado o de la webcam)
    cap = cv.VideoCapture(videoPath)
    return cap


def mostrarVideo(video):
    frames = [] # Array para guardar el video
    
    if not video.isOpened(): # Da "false" cuando no encuentra la cámara
        exit()
    
    ret = True
    while ret:          
        ret, frame = video.read()   # Obtiene un booleano (ret) que dice si se ha leido bien la imagen (al terminar el video devuelve false). Obtiene cada imagen del video (frame)
        
        fps = 30.0
        delay = int(1000/(fps*2))   # Tiempo de espera en "ms" entre frames (se multiplica x2 para que cuadre)
        
        if ret:
            cv.imshow('Nombre_Video',frame)     # Muestra cada imagen del video (formando el video)
            frames.append(frame)                # Guarda cada frame del video
        
        if cv.waitKey(delay) == ord('q'):       # si el usuario pulsa "q", sale del bucle (se para el video)
            break

    return frames
    

def writeVideo(frames, root, nombre):
    outPath = os.path.join(root, nombre)
    
    fourcc = cv.VideoWriter_fourcc(*'XVID')     # Formato del video (MP4)
    fps = 30.0                                  # FPS que quiero guardarlo
    frame_size = (640,480)                      # Tamaño del Frame a guardar
    
    out = cv.VideoWriter(outPath,fourcc,fps,frame_size)     # Objeto del video a Guardar

    # Se lee el video que queremos guardar y guardamos cada uno de sus frames
    for frame in frames:

        out.write(frame)    # Guardamos (o sobrescribimos) los frames en el path mencionado
            
    out.release()       # Obligatorio cerrar el objeto del video a guardar
    
if __name__ == '__main__':
    root = os.getcwd()
    imgPath = os.path.join(root, 'Nombre_Video.avi')

    video = readVideo(imgPath)    # O pongo el path del video o pongo el número de la webcam
    
    frames = mostrarVideo(video)
    
    writeVideo(frames, root, 'Nombre_Video_Guardar.avi')
    
    video.release()     # Obligatorio cerrar el objeto del video
    cv.destroyAllWindows()  # Cerrar todas las ventanas