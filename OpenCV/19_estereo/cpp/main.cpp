#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ auto L=cv::imread("left.png",0),R=cv::imread("right.png",0); if(L.empty()||R.empty()) return 1; auto s=cv::StereoSGBM::create(0,16*8,5,8*25,32*25,1,63,10,100,2,cv::StereoSGBM::MODE_SGBM_3WAY); cv::Mat d16,d; s->compute(L,R,d16); d16.convertTo(d,CV_32F,1.0/16.0); std::cout<<"disp "<<d.size()<<"\n"; }
