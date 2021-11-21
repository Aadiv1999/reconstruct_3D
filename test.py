import cv2
import numpy as np
from matplotlib import pyplot as plt




imgL = cv2.imread('left/left1.jpg')
imgR = cv2.imread('/home/aadiv/Documents/WPI/Fall 21/RBE 549 - Computer Vision/Project/right/right1.jpg')



# stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
# disparity = stereo.compute(imgL,imgR)

# plt.imshow(disparity,'gray')
# plt.show()

# print("Success")