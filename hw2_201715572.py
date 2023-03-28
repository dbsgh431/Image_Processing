import cv2
import numpy as np

# def putText_factory(frame, text, x,y, font=cv2.FONT_HERSHEY_PLAIN, fontsize=3, color=(0,255,255), thickness=2):
#     cv2.putText(frame, text,(x,y),font,fontsize,color,thickness)



cap_rain = cv2.VideoCapture('data/lec6_raining.mp4')
cap_woman = cv2.VideoCapture('data/lec6_woman.mp4')



h = round(cap_woman.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = round(cap_woman.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_count = int(cap_woman.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap_woman.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
delay = round(1000/fps) #ms

video_writer = cv2.VideoWriter()

out = cv2.VideoWriter('lec6_output.avi', fourcc, fps, (w,h))

mode = True
for i in range(frame_count):
    ret_w, frame_w = cap_woman.read()
    ret_r, frame_r = cap_rain.read()

    if ret_w:
        key = cv2.waitKey(delay)
        if key == 27:
            break
        
        if key == 32:
            mode = not mode

        if mode == True:
            mode_str = "On"
            cv2.putText(frame_w,"201715572 KIM YOONHO",(20,30), cv2.FONT_HERSHEY_PLAIN,3,(0,255,255))
            cv2.putText(frame_w,"Chroma key mode:"+mode_str,(20,60), cv2.FONT_HERSHEY_PLAIN,3,(0,255,255))
            cv2.putText(frame_w,"Frame ID:"+f'{i}',(20,100), cv2.FONT_HERSHEY_PLAIN,3,(0,255,255))
            print("mode :", mode)
            out.write(frame_w)
            cv2.imshow("window", frame_w)
        else:
            mode_str = "Off"
            cv2.putText(frame_r,"201715572 KIM YOONHO",(20,30), cv2.FONT_HERSHEY_PLAIN,3,(0,255,255), 2)
            cv2.putText(frame_r,"Chroma key mode:"+mode_str,(20,60), cv2.FONT_HERSHEY_PLAIN,3,(0,255,255), 2)
            cv2.putText(frame_r,"Frame ID:"+f'{i}',(20,100), cv2.FONT_HERSHEY_PLAIN,3,(0,255,255), 2)
            out.write(frame_r)
            print("mode :", mode)
            cv2.imshow("window", frame_r) 

    else:
        break