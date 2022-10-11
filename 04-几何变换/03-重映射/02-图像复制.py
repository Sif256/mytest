# coding: utf-8
# filename: 02-图像复制
# develop: sif
# date: 2022-09-29 15:58

# 读取图像，构造mapx和mapy，实现图像复制
import cv2
import numpy as np
img = cv2.imread('JR.jpg', 1)
line, col = img.shape[:2]
# 构造mapx与mapy
mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)
for i in range(line):
    for j in range(col):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)

# 重映射
rst = cv2.remap(img, mapx, mapy, interpolation=cv2.INTER_LINEAR)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
