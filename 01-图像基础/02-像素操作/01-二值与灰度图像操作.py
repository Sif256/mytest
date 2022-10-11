# coding: utf-8
# filename: 01-二值与灰度图像操作
# develop: sif
# date: 2022-09-27 09:06

# 灰度图像操作
import cv2
img = cv2.imread("nightingale.jpg", 1)
# 读取
print(img[10, 12])
# 修改
img[10, 12] = 255
print(img[10, 12])
# 修改一个区域
for i in range(100):
    for j in range(100):
        img[i, j] = 0
# 显示结果
cv2.imshow("n", img)
cv2.waitKey()
cv2.destroyAllWindows()
