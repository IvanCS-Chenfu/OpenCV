#include <open3d/Open3D.h>
#include <iostream>
int main(){ open3d::pipelines::registration::PoseGraph pg; pg.nodes_.emplace_back(Eigen::Matrix4d::Identity()); std::cout<<"Construye nodos/aristas y ejecuta GlobalOptimization; ver wiki.\n"; }
