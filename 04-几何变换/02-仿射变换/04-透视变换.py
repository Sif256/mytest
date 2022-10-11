# coding: utf-8
# filename: 04-透视变换
# develop: sif
# date: 2022-09-29 11:58

# 读取一幅图像，进行透视变化
import cv2
import numpy as np
img = cv2.imread('book.png', 1)
line, col = img.shape[:2]
# 构造m矩阵
p_1 = np.float32([[374, 7], [610, 62], [22, 167], [286, 357]])
p_2 = np.float32([[0, 0], [300, 0], [0, 500], [300, 500]])
m = cv2.getPerspectiveTransform(p_1, p_2)
# 透视
rst = cv2.warpPerspective(img, m, (300, 500))
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
