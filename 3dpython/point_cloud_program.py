import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d

# %matplotlib auto

file_data_path = "/mnt/c/Users/juneg/OneDrive/PhD/3d_tutorials/data/sample.xyz"
point_cloud = np.loadtxt(file_data_path, skiprows=1, max_rows=None)

xyz=point_cloud[:, :3]
rgb=point_cloud[:, 3:6]

mean_Z = np.mean(point_cloud,axis=0)[2]
spatial_query=point_cloud[abs(point_cloud[:,2]-mean_Z)<1]

# ax=plt.axes(projection='3d')
# ax.scatter(xyz[:,0], xyz[:,1],xyz[:,2], c=rgb/255, s=0.01)
# plt.show()

np.savetxt("/mnt/c/Users/juneg/OneDrive/PhD/3d_tutorials/data/sample_filtered.xyz", spatial_query, delimiter=";", fmt='%1.3f')