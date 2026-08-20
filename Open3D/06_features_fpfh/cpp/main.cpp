#include <open3d/Open3D.h>
#include <iostream>
int main(){ auto pc=open3d::io::CreatePointCloudFromFile("input.ply"); if(!pc) return 1; auto down=pc->VoxelDownSample(0.03); down->EstimateNormals(open3d::geometry::KDTreeSearchParamHybrid(0.06,30)); auto f=open3d::pipelines::registration::ComputeFPFHFeature(*down,open3d::geometry::KDTreeSearchParamHybrid(0.15,100)); std::cout<<f->data_.rows()<<"x"<<f->data_.cols()<<"\n"; }
