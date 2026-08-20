#include <open3d/Open3D.h>
#include <random>
int main(){ auto pc=std::make_shared<open3d::geometry::PointCloud>(); std::mt19937 g(7); std::normal_distribution<double>d; for(int i=0;i<5000;i++) pc->points_.emplace_back(d(g),d(g),d(g)); open3d::io::WritePointCloud("output.ply",*pc); }
