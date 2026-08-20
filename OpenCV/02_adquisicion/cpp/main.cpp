#include <opencv2/opencv.hpp>
#include <stdexcept>
int main(){ cv::VideoCapture cap(0); if(!cap.isOpened()) throw std::runtime_error("No se pudo abrir la cámara"); cv::Mat frame; while(cap.read(frame)){ cv::imshow("camara",frame); int k=cv::waitKey(1); if(k==27 || k=='q') break; } }
