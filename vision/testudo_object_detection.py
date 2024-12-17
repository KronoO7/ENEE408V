from ultralytics import YOLO
from picamera2 import Picamera2
import cv2
from matplotlib import pyplot as plt

def init_camera():
    picam2 = Picamera2()
    # picam2.preview_configuration.main.size = (640,640)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()
    model = YOLO('/home/team_usa/enee408v/vision/best (4).pt')
    return picam2, model

# while True:
def detectTestudo(picam2, model):
    frame =  picam2.capture_array()

    results = model.predict(frame, conf = .6)

    annotated_frame = results[0].plot()

    inference_time = results[0].speed['inference']
    fps = 1000/inference_time
    text = f'FPS: {fps:.1f}'

    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = annotated_frame.shape[1] - text_size[0] - 10
    text_y = text_size[1] + 10

    cv2.putText(annotated_frame, text, (text_x, text_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imwrite("testudo.jpg", annotated_frame)
    # cv2.imshow('output', annotated_frame  )
    #plt.imshow(annotated_frame)
    # cv2.waitKey(200)

    # if cv2.waitKey(1) == ord("q"):
        # break

    return results[0], results[0].boxes.cls.tolist()


picam2, model = init_camera()
while True:
    results, boxes = (detectTestudo(picam2, model))
    print(boxes)
    print(results.boxes.xywh)
