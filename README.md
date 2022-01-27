## 3D Recontruction Using Stereo Vision
This Project consists implementation of creating 3D pointclouds from the Left and Right Images of a Stereo Camera.
The main idea is to use the epipolar geometry and Simple Pinhole Camera model to estimate the depth of points in the Image.
A disparity map is created using feature matching algorithms like SIFT, SURF, ORB etc. In this we have used the OpenCv function to Stereo_BM to create the disparity map.
The depth map is then created using the Camera parameters data.

**DATASET USED:**
https://vision.middlebury.edu/stereo/data/scenes2014/

![Dataset Sample](https://github.com/Aadiv1999/reconstruct_3D/blob/main/outputs/stereo%20pair.png)

The file **3D_Reconstruction.ipynb** consists the complete implementation of the project.

The outputs are saved in .pcd file format which is then visualized using MATLAB.

# Outputs
**Disparity** 
<!-- ![disp1]() -->
**Depth**
**PointClouds**

![output1](https://github.com/Aadiv1999/reconstruct_3D/blob/main/images/reconstruct1.gif)
![output2](https://github.com/Aadiv1999/reconstruct_3D/blob/main/images/reconstruct2.gif)
