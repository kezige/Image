#encoding:utf-8

import numpy as np
import cv2

image = cv2.imread("bbb.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)

#高斯滤波
blurred = np.hstack([cv2.GaussianBlur(image,(3,3),0),
                     cv2.GaussianBlur(image,(5,5),0),
                     cv2.GaussianBlur(image,(7,7),0)
                     ])
cv2.imshow("Gaussian",blurred)
cv2.waitKey(0)