#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ auto b=cv::imread("binary.png",cv::IMREAD_GRAYSCALE); if(b.empty()) return 1; std::vector<std::vector<cv::Point>> c; cv::findContours(b,c,cv::RETR_EXTERNAL,cv::CHAIN_APPROX_SIMPLE); std::cout<<"contornos "<<c.size()<<"\n"; for(size_t i=0;i<c.size()&&i<10;i++) std::cout<<i<<" area "<<cv::contourArea(c[i])<<" perimetro "<<cv::arcLength(c[i],true)<<"\n"; }
