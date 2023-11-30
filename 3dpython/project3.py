import numpy as np
import open3d as o3d

input_path="/mnt/c/Users/juneg/OneDrive/PhD/3d_tutorials/data/3dpython_data/"
output_path="/mnt/c/Users/juneg/OneDrive/PhD/3d_tutorials/3dpython/outputs/"
dataname="sample.xyz"
point_cloud= np.loadtxt(input_path+dataname,skiprows=1)

# transform the point_cloud variable type from Numpy to the Open3D o3d.geometry.
# PointCloud type for further processing:

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])

o3d.visualization.draw_geometries([pcd])
