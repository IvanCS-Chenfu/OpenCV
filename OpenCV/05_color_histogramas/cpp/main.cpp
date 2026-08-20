#include <opencv2/opencv.hpp>
int main(){ auto img=cv::imread("input.jpg"); if(img.empty()) return 1; cv::Mat hsv,g,eq,cl; cv::cvtColor(img,hsv,cv::COLOR_BGR2HSV); cv::cvtColor(img,g,cv::COLOR_BGR2GRAY); cv::equalizeHist(g,eq); cv::createCLAHE(2.0,{8,8})->apply(g,cl); cv::imwrite("output_equalized.png",eq); cv::imwrite("output_clahe.png",cl); }
