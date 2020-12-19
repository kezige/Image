import cv2
import copy
import random
import imutils
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread('123.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)  # 转换格式
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)  # 转换成HSV格式
img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)  # 转换成HSL格式

# 使用opencv自带函数实现，使用上述laplacian模板1
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# 定义了卷积核，对每一个像素进行操作
lapkernel_img1 = cv2.filter2D(img_bgr, -1, kernel)
lap_img1 = img_bgr - lapkernel_img1

# 使用opencv自带函数实现，使用上述laplacian模板1
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# 定义了卷积核，对每一个像素进行操作
lapkernel_img2 = cv2.filter2D(img_hsv, -1, kernel)
lap_img2 = img_hsv - lapkernel_img2

# 使用opencv自带函数实现，使用上述laplacian模板1
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# 定义了卷积核，对每一个像素进行操作
lapkernel_img3 = cv2.filter2D(img_rgb, -1, kernel)
lap_img3 = img_rgb - lapkernel_img3

# 使用opencv自带函数实现，使用上述laplacian模板1
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# 定义了卷积核，对每一个像素进行操作
lapkernel_img4 = cv2.filter2D(img_hls, -1, kernel)
lap_img4 = img_hls - lapkernel_img4


cv2.imshow('origin image', imutils.resize(img_bgr, 400))
cv2.imshow('bgr', imutils.resize(lap_img1, 400))
cv2.imshow('hsv', imutils.resize(lap_img2, 400))
cv2.imshow('rgb', imutils.resize(lap_img3, 400))
cv2.imshow('hls', imutils.resize(lap_img4, 400))
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

