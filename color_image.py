import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('123.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)  # 转换格式
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)  # 转换成HSV格式
img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)  # 转换成HSL格式
# plt.figure(figsize=(8, 5))
plt.subplot(221)
plt.imshow(img_rgb)
plt.title('RGB')
plt.subplot(222)
plt.imshow(img_bgr)
plt.title('BGR')
plt.subplot(223)
plt.imshow(img_hls)
plt.title('HLS')
plt.subplot(224)
plt.imshow(img_hsv)
plt.title('HSV')

plt.show()