# coding: utf-8
# filename: 01-腐蚀
# develop: sif
# date: 2022-09-30 12:03

# 生成一幅图像，进行腐蚀
import cv2
import numpy as np
img = np.zeros((5, 5), np.uint8)
img[1:4, 1:4] = 1
# 创建结构元
kernel = np.ones((3, 1), np.uint8)
# 腐蚀
rst = cv2.erode(img, kernel)
print('img=\n', img)
print('kernel=\n', kernel)
print('rst=\n', rst)
