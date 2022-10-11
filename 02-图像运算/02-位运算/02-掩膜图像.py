# coding: utf-8
# filename: 02-掩膜图像
# develop: sif
# date: 2022-09-28 08:59

# 读取一幅图像，图像自加，显示结果
import cv2
import numpy as np

img = cv2.imread('nightingale.jpg', 1)
mask = np.zeros(img.shape[:2], dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 1
# 加法运算
rst = cv2.add(img, img, mask=mask)
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
