#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ cv::Mat K=(cv::Mat_<double>(3,3)<<700,0,320,0,700,240,0,0,1); cv::Vec3d r(0.05,-0.1,0.02), t(0,0,4); std::vector<cv::Point3f> p={{-1,-1,0},{1,-1,0},{1,1,0},{-1,1,0},{0,0,1}}; std::vector<cv::Point2f> uv; cv::projectPoints(p,r,t,K,cv::noArray(),uv); for(auto &q:uv) std::cout<<q<<"\n"; }
