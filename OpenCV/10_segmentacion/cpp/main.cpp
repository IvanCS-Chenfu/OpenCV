#include <opencv2/opencv.hpp>
int main(){ auto g=cv::imread("input.jpg",cv::IMREAD_GRAYSCALE); if(g.empty()) return 1; cv::Mat o,a; cv::threshold(g,o,0,255,cv::THRESH_BINARY|cv::THRESH_OTSU); cv::adaptiveThreshold(g,a,255,cv::ADAPTIVE_THRESH_GAUSSIAN_C,cv::THRESH_BINARY,31,5); cv::imwrite("output_otsu.png",o); cv::imwrite("output_adaptive.png",a); }
