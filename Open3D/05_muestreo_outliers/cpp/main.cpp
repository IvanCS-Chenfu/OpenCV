#include <open3d/Open3D.h>
#include <iostream>
int main(){ auto pc=open3d::io::CreatePointCloudFromFile("input.ply"); if(!pc) return 1; auto down=pc->VoxelDownSample(0.02); auto result=down->RemoveStatisticalOutliers(30,2.0); auto clean=std::get<0>(result); std::cout<<pc->points_.size()<<" -> "<<clean->points_.size()<<"\n"; open3d::io::WritePointCloud("clean.ply",*clean); }
