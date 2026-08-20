#include <open3d/Open3D.h>
int main(){ auto m=open3d::io::CreateMeshFromFile("mesh.ply"); if(!m) return 1; m->ComputeVertexNormals(); auto p=m->SamplePointsPoissonDisk(5000); open3d::io::WritePointCloud("sampled.ply",*p); }
