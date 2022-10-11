# coding: utf-8
# filename: 01-数字水印嵌入和提取
# develop: sif
# date: 2022-09-28 11:00

# 读取一幅图像，进行二值图像嵌入
# 提取水印图像
import cv2
import numpy as np
# 载体图像
img = cv2.imread('lena.bmp', 1)
row, col, d = img.shape
# 水印图像
water = cv2.imread('water.bmp', 1)
w = water[:, :, :] > 0
water[w] = 1
# 嵌入水印
t_254 = np.ones(img.shape, dtype=np.uint8)*254
h_7 = cv2.bitwise_and(img, t_254)
into = cv2.bitwise_or(h_7, water)
# 提取水印
t_1 = np.ones(img.shape, dtype=np.uint8)
out = cv2.bitwise_and(into, t_1)
# 阈值处理
m = out[:, :, :] > 0
out[m] = 255
# 显示结果
cv2.imshow('img', h_7)
cv2.imshow('water', water*255)
cv2.imshow('into', into)
cv2.imshow('out', out)
cv2.waitKey()
cv2.destroyAllWindows()
