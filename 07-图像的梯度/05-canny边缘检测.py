# coding: utf-8
# filename: 05-canny边缘检测
# develop: sif
# date: 2022-10-05 12:17

# 读取图像，进行canny检测，显示结果
import cv2
img = cv2.imread('JR.jpg', 1)
# 高斯滤波去噪
rst = cv2.GaussianBlur(img, (5, 5), 0, 0)
# canny检测
rst_1 = cv2.Canny(rst, 132, 200)
rst_2 = cv2.Canny(rst, 30, 132)
# 显示结果
cv2.imshow('img', img)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
