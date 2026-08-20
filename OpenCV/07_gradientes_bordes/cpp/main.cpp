#include <opencv2/opencv.hpp>
int main(){ auto g=cv::imread("input.jpg",cv::IMREAD_GRAYSCALE); if(g.empty()) return 1; cv::Mat gx,gy,e; cv::Sobel(g,gx,CV_32F,1,0); cv::Sobel(g,gy,CV_32F,0,1); cv::Canny(g,e,80,160); cv::imwrite("output_canny.png",e); }
