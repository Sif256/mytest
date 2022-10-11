# coding: utf-8
# filename: 03-最小的矩形框
# develop: sif
# date: 2022-10-06 16:05

# 读取一幅图像，获取轮廓，进行最小矩形框轮廓的拟合
import cv2
import numpy as np
img = cv2.imread('cc.png', 1)
# 转为灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 转为二值图
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 获取最小矩形框
rect = cv2.minAreaRect(contours[0])
point = cv2.boxPoints(rect)
point = np.int0(point)
print(point)
# 绘制矩形框
cv2.drawContours(img, [point], -1, (111, 33, 135), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
