#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ cv::Mat img(360,640,CV_8UC3,cv::Scalar(0,0,0)); img(cv::Rect(0,0,320,360)).setTo(cv::Scalar(255,0,0)); img(cv::Rect(320,0,320,360)).setTo(cv::Scalar(0,180,255)); cv::Rect r(220,80,200,200); cv::rectangle(img,r,cv::Scalar(255,255,255),2); std::cout << img.cols << "x" << img.rows << " type=" << img.type() << "\n"; cv::imwrite("output_fundamentos.png",img); }
