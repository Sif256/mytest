# coding: utf-8
# filename: 02-脸部打码
# develop: sif
# date: 2022-09-27 14:23

# 读取图像，修改感兴趣区域
import cv2
import numpy as np
img = cv2.imread('nightingale.jpg', 1)
exam = img[250:520, 170:420]
code = np.random.randint(0, 256, size=[270, 250, 3], dtype=np.uint8)
img[250:520, 170:420] = code
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
