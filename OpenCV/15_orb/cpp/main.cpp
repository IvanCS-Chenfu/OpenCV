#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ auto g=cv::imread("input.jpg",cv::IMREAD_GRAYSCALE); if(g.empty()) return 1; auto o=cv::ORB::create(1000,1.2f,8); std::vector<cv::KeyPoint> k; cv::Mat d,out; o->detectAndCompute(g,cv::noArray(),k,d); cv::drawKeypoints(g,k,out); std::cout<<k.size()<<" keypoints\n"; cv::imwrite("output_orb.png",out); }
