#include <opencv2/opencv.hpp>
#include <fstream>
#include <iostream>
int main(){ std::ifstream a("points1.txt"),b("points2.txt"); std::vector<cv::Point2f> p1,p2; float x,y; while(a>>x>>y) p1.emplace_back(x,y); while(b>>x>>y) p2.emplace_back(x,y); if(p1.size()!=p2.size()||p1.size()<8) return 1; cv::Mat mask; auto F=cv::findFundamentalMat(p1,p2,cv::FM_RANSAC,1.0,0.999,mask); std::cout<<"F=\n"<<F<<"\ninliers="<<cv::countNonZero(mask)<<"\n"; }
