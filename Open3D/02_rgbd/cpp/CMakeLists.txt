cmake_minimum_required(VERSION 3.16)
project(open3d_02_rgbd LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
find_package(Open3D REQUIRED)
add_executable(open3d_02_rgbd main.cpp)

target_link_libraries(open3d_02_rgbd PRIVATE Open3D::Open3D)
