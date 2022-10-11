# coding: utf-8
# filename: 01-获取感兴趣区域
# develop: sif
# date: 2022-09-27 14:14

import cv2
img = cv2.imread('nightingale.jpg', 1)
exam = img[250:520, 170:420]
img[0:270, 0:250] = exam
cv2.imshow('exam', img)
cv2.waitKey()
cv2.destroyAllWindows()
