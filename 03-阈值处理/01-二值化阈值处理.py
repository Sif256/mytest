# coding: utf-8
# filename: 01-二值化阈值处理
# develop: sif
# date: 2022-09-28 14:06

# 生成一个灰度图像，对其进行阈值处理
import cv2
import numpy as np
img = np.random.randint(0, 256, size=[2, 4], dtype=np.uint8)
# 阈值处理
var, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 显示结果
print(var)
print('img=\n', img)
print('rst=\n', rst)
