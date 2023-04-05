import cv2
import numpy as np

def putText_factory(frame, text_userInfo, text_mode, text_frame_count, x,y, font=cv2.FONT_HERSHEY_PLAIN, fontsize=3, color=(0,255,255), thickness=2):
    cv2.putText(frame, text_userInfo,(x,y),font,fontsize,color,thickness)
    cv2.putText(frame, text_mode,(x,y+40),font,fontsize,color,thickness)
    cv2.putText(frame, text_frame_count,(x,y+80),font,fontsize,color,thickness)

cap_rain = cv2.VideoCapture('data/lec6_raining.mp4')
cap_woman = cv2.VideoCapture('data/lec6_woman.mp4')

h = int(cap_woman.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(cap_woman.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_count = int(cap_woman.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap_woman.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
delay = round(1000/fps) #ms

out = cv2.VideoWriter('lec6_output.avi', fourcc, fps, (w,h))

mode = True

for i in range(frame_count):
    ret_w, frame_w = cap_woman.read()
    ret_r, frame_r = cap_rain.read()
    
    hsv = cv2.cvtColor(frame_w, cv2.COLOR_BGR2HSV)

    # threshold
    lower_green = np.array([50, 50, 50])
    upper_green = np.array([65, 255, 255]) 


    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    green_object = cv2.bitwise_and(frame_r, frame_r, mask=mask)
    background = cv2.bitwise_and(frame_w, frame_w, mask=mask_inv)

    result = cv2.add(green_object, background)

    
    if ret_w:
        key = cv2.waitKey(delay)

        if key == 27:
            break
        
        if key == 32:
            mode = not mode

        if mode:
            mode_str = "On"
            putText_factory(result,"201715572 KIM YOONHO","Chroma key mode:"+mode_str,"Frame ID:"+f'{i+1}',20,30)
            out.write(result)
            cv2.imshow("window", result)

        else:
            mode_str = "Off"
            putText_factory(frame_w,"201715572 KIM YOONHO","Chroma key mode:"+mode_str,"Frame ID:"+f'{i+1}',20,30)
            out.write(frame_w)
            cv2.imshow("window", frame_w) 

    else:
        break


cap_rain.release()
cap_woman.release()
out.release()
cv2.destroyAllWindows()