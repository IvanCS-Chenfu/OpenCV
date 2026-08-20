#include <open3d/Open3D.h>
int main(){ auto pc=open3d::io::CreatePointCloudFromFile("input.ply"); if(!pc) return 1; pc->EstimateNormals(open3d::geometry::KDTreeSearchParamHybrid(0.05,30)); pc->OrientNormalsConsistentTangentPlane(20); open3d::io::WritePointCloud("normals.ply",*pc); }
