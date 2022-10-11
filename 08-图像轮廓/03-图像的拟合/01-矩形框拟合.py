# coding: utf-8
# filename: 01-矩形框拟合
# develop: sif
# date: 2022-10-06 12:07

# 读取一幅图像，对其进行矩形框的拟合，绘制并显示
import cv2
import numpy as np
img = cv2.imread('cc.png', 0)
img_1 = cv2.imread('cc.png', 1)
# 转为二值图
binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 获取坐标数据
x, y, w, h = cv2.boundingRect(contours[0])
cut = np.array([[x, y], [x + w, y], [x + w, y + h], [x, y + h]])
# 绘制矩形框
cv2.drawContours(img_1, [cut], -1, (111, 9, 215), 2)
cv2.imshow('img', img)
cv2.imshow('img_1', img_1)
cv2.waitKey()
cv2.destroyAllWindows()
