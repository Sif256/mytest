# coding: utf-8
# filename: 02-彩色图像访问与修改
# develop: sif
# date: 2022-09-27 13:53

# 随机生成一个彩色图像并用item与itemset对其访问与修改
import cv2
import numpy as np

img = np.random.randint(0, 256, size=[5, 5, 3], dtype=np.uint8)
# 显示图像
# print('pre:\n', img)
# print(img[0, 3])
# print(img[0, 3, 1])
# 修改像素
# img[0, 3] = [128, 128, 128]
# img.itemset((0, 3, 2), 0)
# print('after:\n', img)
# 使用随机函数生产彩色图片
img_1 = np.random.randint(0, 256, size=[300, 300, 3], dtype=np.uint8)
img_1[100:200, 100:200] = [177, 45, 89]
cv2.imshow('img_1', img_1)
cv2.waitKey()
cv2.destroyAllWindows()
