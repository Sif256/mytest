# coding: utf-8
# filename: 01-加法运算
# develop: sif
# date: 2022-09-27 15:27

# 读取图像，进行加法运算，显示结果
import cv2
img_1 = cv2.imread('nightingale.jpg', 1)
# 加号运算
rst_1 = img_1 + img_1
# add函数加法运算
rst_2 = cv2.add(img_1, img_1)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
