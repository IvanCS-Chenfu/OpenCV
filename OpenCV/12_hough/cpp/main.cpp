#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ auto g=cv::imread("input.jpg",cv::IMREAD_GRAYSCALE); if(g.empty()) return 1; cv::Mat e; cv::Canny(g,e,80,160); std::vector<cv::Vec4i> l; cv::HoughLinesP(e,l,1,CV_PI/180,80,50,10); std::cout<<"lineas "<<l.size()<<"\n"; }
