# coding: utf-8
# filename: 03-灵活的仿射变换
# develop: sif
# date: 2022-09-29 11:39

# 读取一幅图像，进行源图像和目标图像3个顶点，进行仿射变换
import cv2
import numpy as np
img = cv2.imread('JR.jpg', 1)
line, col = img.shape[:2]
# 构造m矩阵
p_1 = np.float32([[0, 0], [col-1, 0], [0, line-1]])
p_2 = np.float32([[0, line*0.33], [col*0.77, line*0.15], [col*0.35, line*0.85]])
m = cv2.getAffineTransform(p_1, p_2)
rst = cv2.warpAffine(img, m, (col, line))
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
