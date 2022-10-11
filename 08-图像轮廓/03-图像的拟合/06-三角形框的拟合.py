# coding: utf-8
# filename: 06-三角形框的拟合
# develop: sif
# date: 2022-10-06 17:17

# 读取一幅图像，获取轮廓，进行椭圆框轮廓的拟合
import cv2
import numpy as np
img = cv2.imread('cc.png', 1)
# 转为灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 转为二值图
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 获取三角形面积和顶点
var, trilange = cv2.minEnclosingTriangle(contours[0])
tril = np.int0(trilange)
print(tril)
for i in range(3):
    cv2.line(img, tuple(tril[i][0]), tuple(tril[(i + 1) % 3][0]), (212, 24, 77), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
