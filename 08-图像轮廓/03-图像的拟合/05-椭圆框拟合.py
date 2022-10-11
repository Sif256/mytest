# coding: utf-8
# filename: 05-椭圆框拟合
# develop: sif
# date: 2022-10-06 16:54

# 读取一幅图像，获取轮廓，进行椭圆框轮廓的拟合
import cv2
img = cv2.imread('cc.png', 1)
# 转为灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 转为二值图
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 获取椭圆
ellipse = cv2.fitEllipse(contours[0])
# 绘制矩形框
cv2.ellipse(img, ellipse, (21, 12, 127), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
