# coding: utf-8
# filename: 03-彩色通道颜色
# develop: sif
# date: 2022-09-27 09:43

# 创建一个三维数组模拟彩色图像
import cv2
import numpy as np
img = np.zeros((300, 300, 3), dtype=np.uint8)
# 修改颜色通道
img[:, 0:100, 0] = 255
img[:, 100:200, 1] = 255
img[:, 200:300, 2] = 255
# 显示结果
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
