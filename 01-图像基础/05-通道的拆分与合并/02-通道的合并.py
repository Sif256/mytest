# coding: utf-8
# filename: 02-通道的合并
# develop: sif
# date: 2022-09-27 15:01

# 读取图像，进行通道的拆分与合并
import cv2
img = cv2.imread('nightingale.jpg', 1)
b, g, r = cv2.split(img)
rgb = cv2.merge([r, g, b])
grb = cv2.merge([g, r, b])
bgr = cv2.merge([b, g, r])
cv2.imshow('rgb', rgb)
cv2.imshow('grb', grb)
cv2.imshow('bgr', bgr)
cv2.waitKey()
cv2.destroyAllWindows()
