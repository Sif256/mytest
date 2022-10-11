# coding: utf-8
# filename: 02-彩色图像通道颜色
# develop: sif
# date: 2022-09-27 09:21

# 使用np生成一个三维数组表示一个彩色图像，修改通道，显示结果
import cv2
import numpy as np
blue = np.zeros((300, 300, 3), dtype=np.uint8)
# 修改蓝色通道
blue[:, :, 0] = 255
# 显示结果
cv2.imshow('blue', blue)
# 修改绿色通道
green = np.zeros((300, 300, 3), dtype=np.uint8)
green[:, :, 1] = 255
# 显示结果
cv2.imshow('green', green)
# 修改红色通道
red = np.zeros((300, 300, 3), dtype=np.uint8)
red[:, :, 2] = 255
# 显示结果
cv2.imshow('red', red)
cv2.waitKey()
cv2.destroyAllWindows()
