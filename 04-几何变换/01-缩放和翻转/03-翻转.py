# coding: utf-8
# filename: 03-翻转
# develop: sif
# date: 2022-09-28 15:51


# 读取一幅图像，进行水平和垂直方向翻转
import cv2
img = cv2.imread('JR.jpg', 1)
# 翻转
rst = cv2.flip(img, 1)
rst_1 = cv2.flip(img, 0)
rst_2 = cv2.flip(img, -1)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst-2', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
