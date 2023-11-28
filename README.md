## 영상처리 과제 토이 프로젝트


## 마우스 입력을 이용한 객체 바운딩 박스 이미지 생성 모듈 ( Draw_Bbox.py )

![lec4_vehicles](https://github.com/dbsgh431/Image_Processing/assets/39187226/f944ddab-247a-4072-82dc-13939fe86f28)
<div>원본</div>
<br></br>

![hw1_output](https://github.com/dbsgh431/Image_Processing/assets/39187226/f26a1497-e52f-40b1-9d9c-6f70fce38e83)
<div>바운딩 박스 생성 후</div>

<p>
  <h5>구현 내용</h5>
  1. 바운딩 박스를 그릴 이미지 경로 수정(cv2.imread)<br/>
  2. 좌클릭으로 직사각형의 대각선 두 점의 좌표씩 입력<br/>
  3. 우클릭으로 입력을 종료 후 결과 이미지(hw1_output.jpg)를 생성</p>


## 키보드 입력을 통한 크로마키 합성 영상 제작 모듈 ( Chroma_Key.py )

![chroma_key](https://github.com/dbsgh431/Image_Processing/assets/39187226/99a2663e-ae87-461c-9a2a-e9413acd1f39)

<p>키보드 입력을 통한 크로마키 객체 영상, 배경 영상을 이용한 크로마키 합성 영상 모듈<br/><br/>
  1. 실행 중 키보드 space 입력을 통해 객체 배경 합성, 합성 해제<br/> 
  2. 1번 과정을 동영상으로 생성
</p>

## 두 이미지의 weighted sum을 통한 합성 영상 생성 모듈 ( Image_weightedSum.py)

![weightedsum](https://github.com/dbsgh431/Image_Processing/assets/39187226/f326dba9-8c44-4123-9234-43e2bec90ee0)

<p>
  1.처음 이미지에서 1~4초 동안 다른 이미지로의 weighted summation 영상을 거쳐 마지막 1초에 다른 이미지 영상으로 완전히 전환
</p>

## Tesseract OCR 모듈을 활용한 이미지 속 텍스트 추출 ( OCR.py)

![img2text](https://github.com/dbsgh431/Image_Processing/assets/39187226/afd08aa7-6b38-407e-91a1-55063e716125)
<div>원본</div>
<br></br>

![ret](https://github.com/dbsgh431/Image_Processing/assets/39187226/e10724c0-2256-4b53-bc85-528dd44fcffc)
<div>외곽선 탐지를 통한 객체 추출</div>
<br></br>
<p>
  1. 이미지 속 객체 탐지를 위한 이진화<br/>
  2. Opening 모폴로지 연산을 통한 노이즈 제거<br/>
  3. 외곽선 탐지 후 어파인 변환을 통한 이미지 객체 추출<br/>
  4. Tesseract OCR를 사용한 이미지 속 텍스트 추출<br/>
</p>
