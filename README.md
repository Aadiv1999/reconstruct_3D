## 3D Recontruction Using Stereo Vision
This Project consists implementation of creating 3D pointclouds from the Left and Right Images of a Stereo Camera.
The main idea is to use the epipolar geometry and Simple Pinhole Camera model to estimate the depth of points in the Image.

A disparity map is created using feature matching algorithms like SIFT, SURF, ORB, etc. In this we have used the OpenCv function to Stereo_BM to create the disparity map.
The depth map is then created using the Camera parameters data.
This depth map is then Converted to Point Cloud in PCD format using Open3D libraray functions.
