#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ auto g=cv::imread("input.jpg",cv::IMREAD_GRAYSCALE); if(g.empty()) return 1; std::vector<cv::Point2f> c; cv::goodFeaturesToTrack(g,c,300,0.01,8,cv::noArray(),3,true,0.04); std::cout<<"esquinas "<<c.size()<<"\n"; }
