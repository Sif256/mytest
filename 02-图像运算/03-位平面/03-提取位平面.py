# coding: utf-8
# filename: 03-位平面
# develop: sif
# date: 2022-09-28 09:44

# 读取灰度图像，提取8个位平面
import cv2
import numpy as np
# 获取原始图像的属性
img = cv2.imread('JR.jpg', 1)
cv2.imshow('img', img)
row, col, d = img.shape
# 构造提取矩阵
x = np.zeros((row, col, d, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, :, i] = 2**i

# 提取位平面
r = np.zeros((row, col, d, 8), dtype=np.uint8)
for i in range(8):
    r[:, :, :, i] = cv2.bitwise_and(img, x[:, :, :, i])
    # 阈值处理
    mask = r[:, :, :, i] > 0
    r[mask] = 255
    cv2.imshow('wpm_'+str(i), r[:, :, :, i])
cv2.waitKey()
cv2.destroyAllWindows()
