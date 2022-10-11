# coding: utf-8
# filename: 01-彩色图像的拆分
# develop: sif
# date: 2022-09-27 14:51

# 读取一幅彩色图像，进行拆分，显示
import cv2
img = cv2.imread('nightingale.jpg', 1)
# 索引拆分
# b = img[:, :, 0]
# g = img[:, :, 1]
# r = img[:, :, 2]
# 函数拆分
# b, g, r = cv2.split(img)
# 单通道拆分
b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]
# 显示结果
cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()
cv2.destroyAllWindows()
