import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


# 1 Todo name, info text
def putText_factory(src):
    font = ImageFont.truetype("fonts/gulim.ttc", 30)
    org = (20, 20)
    text = "201715572 김윤호"
    src = Image.fromarray(src)
    draw = ImageDraw.Draw(src)
    draw.text(org, text, font=font, fill=(0, 255, 255))
    return np.array(src)


src1 = cv2.imread("data/lec9_Resources/lec9_airplane.bmp")
src2 = cv2.imread("data/lec9_Resources/lec9_field.bmp")

fps = 30

h, w, _ = src1.shape

fourcc = cv2.VideoWriter_fourcc(*"DIVX")

out = cv2.VideoWriter("lec9_output.avi", fourcc, fps, (w, h))


for i in range(fps * 1):
    #src2 = putText_factory(src2)
    out.write(src2)
for j in range(fps * 3):
    # 2 Todo : weighted sum
    beta = float(j / (fps * 3))
    alpha = 1 - beta
    dst = cv2.addWeighted(src2, alpha, src1, beta, gamma=None)
    #dst = putText_factory(dst)
    out.write(dst)
for k in range(fps * 1):
    #src1 = putText_factory(src1)
    out.write(src1)

out.release()
