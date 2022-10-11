# coding: utf-8
# filename: 03-膨胀
# develop: sif
# date: 2022-09-30 12:19

# 生成一幅图像，进行膨胀
import cv2
import numpy as np
img = np.zeros((5, 5), dtype=np.uint8)
img[2:3, 1:4] = 1
# 生成一个结构元
kernel = np.ones((3, 1), np.uint8)
# 膨胀
rst = cv2.dilate(img, kernel)
print('img=\n', img)
print('kernel=\n', kernel)
print('rst=\n', rst)
