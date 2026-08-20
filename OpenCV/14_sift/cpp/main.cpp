#include <opencv2/opencv.hpp>
#include <iostream>
int main(){ auto g=cv::imread("input.jpg",cv::IMREAD_GRAYSCALE); if(g.empty()) return 1; auto s=cv::SIFT::create(); std::vector<cv::KeyPoint> k; cv::Mat d,o; s->detectAndCompute(g,cv::noArray(),k,d); cv::drawKeypoints(g,k,o,cv::Scalar::all(-1),cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS); std::cout<<k.size()<<" keypoints\n"; cv::imwrite("output_sift.png",o); }
