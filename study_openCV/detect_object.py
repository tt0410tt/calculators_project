import cv2
from ultralytics import YOLO

# YOLOv8 모델 로드 (yolov8n 모델은 작은 모델로, 빠르게 동작)
model = YOLO('study_openCV/yolov8n.pt')  # 'yolov8n.pt' 파일이 없으면 자동으로 다운로드됨

# 웹캠 연결
cap = cv2.VideoCapture(0)

print("웹캠이 열렸습니다. 'q' 키를 누르면 종료됩니다.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("웹캠에서 프레임을 읽지 못했습니다.")
        break

    # YOLOv8 모델로 객체 감지
    results = model(frame)

    # 결과를 이미지에 표시
    annotated_frame = results[0].plot()

    # 화면에 표시
    cv2.imshow('YOLOv8 Webcam Detection', annotated_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()

print("웹캠 연결 종료.")
