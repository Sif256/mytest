# coding: utf-8
# filename: 01-图像
# develop: sif
# date: 2022-09-26 15:11

# 读取图像并显示
import cv2
img = cv2.imread("nightingale.jpg", 1)
cv2.imshow("nightingale", img)
rt = cv2.waitKey()
if rt == ord('a'):
    print('关闭窗口！')
cv2.imwrite("d:/nightingale.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 99])
cv2.destroyAllWindows()
