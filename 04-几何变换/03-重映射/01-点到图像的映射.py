# coding: utf-8
# filename: 01-点到图像的映射
# develop: sif
# date: 2022-09-29 12:18

# 获取原始图像的点，映射到目标图像
import cv2
import numpy as np
img = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)
# 构造mapx与mapy
mapx = np.ones(img.shape, np.float32) * 3
mapy = np.zeros(img.shape, np.float32)
# 重映射
rst = cv2.remap(img, mapx, mapy, interpolation=cv2.INTER_LINEAR)
print('img=\n', img)
print('mapx=\n', mapx)
print('mapy=\n', mapy)
print('rst=\n', rst)
