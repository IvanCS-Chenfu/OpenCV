#include <opencv2/opencv.hpp>
#include <iostream>
int main(int argc,char**argv){ if(argc<2){std::cerr<<"uso: ./leer_config config.yaml\n";return 1;} cv::FileStorage fs(argv[1],cv::FileStorage::READ); if(!fs.isOpened()) return 2; double fx=(double)fs["Camera1.fx"]; std::cout<<"fx="<<fx<<"\n"; }
