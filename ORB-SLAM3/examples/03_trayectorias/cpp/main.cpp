#include <fstream>
#include <iostream>
#include <sstream>
int main(int argc,char**argv){ if(argc<2) return 1; std::ifstream f(argv[1]); std::string line; size_t n=0; while(std::getline(f,line)){ if(line.empty()||line[0]=='#') continue; std::istringstream s(line); double t,tx,ty,tz,qx,qy,qz,qw; if(s>>t>>tx>>ty>>tz>>qx>>qy>>qz>>qw) ++n; } std::cout<<"poses="<<n<<"\n"; }
