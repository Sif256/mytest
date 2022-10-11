# coding: utf-8
# filename: 03-图像亮度
# develop: sif
# date: 2022-09-27 17:07

# 读取图像，进行亮度调节
import cv2
img = cv2.imread('nightingale.jpg', 1)
# 亮度调节
rst = cv2.add(img, 100)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
