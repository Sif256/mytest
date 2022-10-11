# coding: utf-8
# filename: 02-逐个绘制
# develop: sif
# date: 2022-10-05 16:57

# 读取图像 查找轮廓 逐个绘制
import cv2
import numpy as np
img = cv2.imread('contours.bmp', 0)
img_1 = cv2.imread('contours.bmp', 1)
# 转为二值图
binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
# 查找轮廓
contour = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

n = len(contour)
cntImg = []
for i in range(n):
    temp = np.zeros(img_1.shape, np.uint8)
    cntImg.append(temp)
    # 绘制轮廓
    if i == 3:
        cv2.drawContours(cntImg[i], contour, i, (0, 0, 255), 2)
        cv2.imshow('lk_' + str(i), cntImg[i])
cv2.waitKey()
cv2.destroyAllWindows()
