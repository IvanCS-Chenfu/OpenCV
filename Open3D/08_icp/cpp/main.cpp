#include <open3d/Open3D.h>
#include <iostream>
int main(){ auto s=open3d::io::CreatePointCloudFromFile("source.ply"), t=open3d::io::CreatePointCloudFromFile("target.ply"); if(!s||!t) return 1; auto r=open3d::pipelines::registration::RegistrationICP(*s,*t,0.05,Eigen::Matrix4d::Identity(),open3d::pipelines::registration::TransformationEstimationPointToPoint()); std::cout<<r.transformation_<<"\n"; }
