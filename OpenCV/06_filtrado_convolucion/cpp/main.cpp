#include <opencv2/opencv.hpp>
int main(){ auto im=cv::imread("input.jpg"); if(im.empty()) return 1; cv::Mat a,b,c; cv::GaussianBlur(im,a,{7,7},1.5); cv::medianBlur(im,b,7); cv::bilateralFilter(im,c,9,75,75); cv::imwrite("output_gaussian.png",a); cv::imwrite("output_median.png",b); cv::imwrite("output_bilateral.png",c); }
