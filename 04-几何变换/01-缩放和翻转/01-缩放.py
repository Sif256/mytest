# coding: utf-8
# filename: 01-缩放
# develop: sif
# date: 2022-09-28 15:15

# 读取一幅图像，进行放大和缩小
import cv2
img = cv2.imread('JR.jpg', 1)
row, col, = img.shape[:2]
# 放大,缩小
dsize = (col*2, row*3)
rst = cv2.resize(img, dsize)
dsize_1 = (int(col*0.2), int(row*0.2))
rst_1 = cv2.resize(img, dsize_1, interpolation=cv2.INTER_AREA)
cv2.imshow('img', img)
cv2.imshow('rst_1', rst_1)
cv2.waitKey()
cv2.destroyAllWindows()
