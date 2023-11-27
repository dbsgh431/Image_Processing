import cv2
import numpy as np
import pytesseract

original = cv2.imread('img2text.jpg', cv2.IMREAD_COLOR)
src = cv2.imread('img2text.jpg', cv2.IMREAD_GRAYSCALE) 
src = cv2.resize(src,(960, 720))
original = cv2.resize(original,(960, 720))

_, dst = cv2.threshold(src,150, 255,cv2.THRESH_BINARY)

dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel=(2, 2))


contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_contours, max_index = 0, 0    
for idx, contour in enumerate(contours):
    if len(contour) > max_contours:
        max_index = idx
        max_contours = len(contour)

contour = contours[max_index]

epsilon = 0.05 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)
img = cv2.drawContours(original, [approx], -1, (0,255,0), thickness=3)
cv2.imshow("img", img)

approx_np = np.float32(approx)
approx_np = approx_np.reshape(4,2)
pts = np.float32([[720,0], [0, 0], [0,480],[720,480]])

pers = cv2.getPerspectiveTransform(approx_np,pts)
ret = cv2.warpPerspective(img, pers, (720,480))
ret = cv2.rotate(src=ret, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
text = pytesseract.image_to_string(ret, lang='eng+kor')

print('==========텍스트 인식 결과==========')
print(text)

cv2.imshow("dst", dst)
cv2.imshow("ret", ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
