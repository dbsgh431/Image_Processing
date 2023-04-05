import cv2
import numpy as np

src1 = cv2.imread('data/lec9_Resources/lec9_airplane.bmp')
src2 = cv2.imread('data/lec9_Resources/lec9_field.bmp')

fps = 30

h, w, _ = src1.shape

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('lec6_output1.avi', fourcc, fps, (w,h))


for i in range(fps*1):
    out.write(src2)
for i in range(fps*3):
    out.write(src2+ src1)
for i in range(fps*1):
    out.write(src1)


out.release()
