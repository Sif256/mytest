# coding: utf-8
# filename: 001-猫脸检测
# develop: sif
# date: 2022-10-10 15:13

# 单张的猫脸检测
import cv2


def demo_face():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 调用级联分级器
    facecade = cv2.CascadeClassifier('data/haarcascade_frontalcatface_extended.xml')
    face = facecade.detectMultiScale(gray)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (32, 155, 122), 2)
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


img = cv2.imread('cat.jpg', 1)
demo_face()
