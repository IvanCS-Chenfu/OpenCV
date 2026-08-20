#include <open3d/Open3D.h>
int main(){ auto pc=open3d::io::CreatePointCloudFromFile("input.ply"); if(!pc) return 1; Eigen::Matrix4d T=Eigen::Matrix4d::Identity(); T(0,3)=0.2; T(2,3)=0.1; pc->Transform(T); open3d::io::WritePointCloud("transformed.ply",*pc); }
