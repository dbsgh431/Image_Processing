import cv2
import numpy as np
import math

original = cv2.imread('./data/paperPhoto20230517165823287.jpg', cv2.IMREAD_COLOR)

src = cv2.imread('./data/paperPhoto20230517165823287.jpg', cv2.IMREAD_GRAYSCALE) 

#src = cv2.resize(src,(960, 680))


_, dst = cv2.threshold(src,175, 255,cv2.THRESH_BINARY)



dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel=(2, 2))



#dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)


    
    
    

contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_contours, max_index = 0, 0    
for idx, contour in enumerate(contours):
    if len(contour) > max_contours:
        max_index = idx
        max_contours = len(contour)

contour = contours[max_index]

epsilon = 0.05 * cv2.arcLength(contour, True)

approx = cv2.approxPolyDP(contour, epsilon, True)
approx_np = np.float32(approx)
approx_np = approx_np.reshape(4,2)
img = cv2.drawContours(original, [approx], -1, (0,255,0), thickness=3)
pts = np.float32([[720,0], [0, 0], [0,480],[720,480]])

pers = cv2.getPerspectiveTransform(approx_np,pts)
dst = cv2.warpPerspective(img, pers, (720,480))


cv2.imshow("dst", dst)
cv2.imshow("img", img)
#cv2.imshow("org",original)
#cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
