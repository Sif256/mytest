# coding: utf-8
# filename: 02-多张人脸
# develop: sif
# date: 2022-10-10 15:17

# 多张的人脸检测
import cv2


def demo_faces():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 调用级联分级器
    facecade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    face = facecade.detectMultiScale(gray, scaleFactor=1.03, minSize=(30, 36), maxSize=(40, 50))
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (32, 155, 122), 2)
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


img = cv2.imread('manyfaces.png', 1)
demo_faces()
