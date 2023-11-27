import cv2
import numpy as np

global target

target = []

def onMouse(event, x, y, flags, param):
    # Todo 1
    # 0. 좌클릭으로 직사각형의 대각선 두 점의 좌표씩 입력
    # 1. 중복 체크를 위해 클릭한 좌표에 점(원) 그리기
    # 2. 이후 입력한 점들을 따라 직사각형으로 표현하기위해 리스트에 입력 순으로 저장

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),2)
        cv2.imshow("original", img)
        target.append([x, y])

    # Todo 2
    # 0. 우클릭으로 입력을 종료 후 결과 이미지를 생성
    # 1. 원본 이미지와 크기가 같은 zeros 행렬 생성
    # 2. 점들을 저장한 리스트를 가져와에 반복문으로 직사각형 그리기
    #   2.1. 직사각형은 2점 당 1개씩 그려지므로 step이 2인 반복문 작성
    #   2.2. 조건에 맞춰 (0,255,0) color의 직사각형 draw
    # 3. 반복문이 종료되면 해당 행렬과 원본 이미지 행렬을 더해 저장(shape이 같으므로 덧셈 가능)
     
    if event == cv2.EVENT_RBUTTONDOWN:
        target_img = np.zeros(img.shape)
        for i in range(0,len(target),2):
            cv2.rectangle(target_img,(target[i][0], target[i][1]), (target[i+1][0], target[i+1][1]),(0,255,0),2)
        cv2.imwrite('hw1_output.jpg',img_copy+target_img)

img = cv2.imread('data/lec4_Resources/lec4_vehicles.jpg', cv2.IMREAD_COLOR)


img_copy = img.copy()

cv2.imshow("original", img)

cv2.setMouseCallback("original", onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()