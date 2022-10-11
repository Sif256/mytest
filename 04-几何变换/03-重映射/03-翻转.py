# coding: utf-8
# filename: 03-翻转
# develop: sif
# date: 2022-09-29 16:09

# 读取图像 用mapx mapy实现图像翻转
import cv2
import numpy as np
img = cv2.imread("JR.jpg", 1)
# 构造mapx mapy
mapx = np.ones(img.shape[:2], np.float32)
mapy = np.ones(img.shape[:2], np.float32)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        mapx.itemset((i, j), img.shape[1]-j-1)
        mapy.itemset((i, j), img.shape[0]-i-1)

rst = cv2.remap(img, mapx, mapy, interpolation=cv2.INTER_LINEAR)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
