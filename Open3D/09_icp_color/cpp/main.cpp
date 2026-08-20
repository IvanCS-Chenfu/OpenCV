#include <open3d/Open3D.h>
#include <iostream>
int main(){ auto s=open3d::io::CreatePointCloudFromFile("source.ply"), t=open3d::io::CreatePointCloudFromFile("target.ply"); if(!s||!t) return 1; s->EstimateNormals(open3d::geometry::KDTreeSearchParamHybrid(0.05,30)); t->EstimateNormals(open3d::geometry::KDTreeSearchParamHybrid(0.05,30)); auto r=open3d::pipelines::registration::RegistrationColoredICP(*s,*t,0.05,Eigen::Matrix4d::Identity()); std::cout<<r.transformation_<<"\n"; }
