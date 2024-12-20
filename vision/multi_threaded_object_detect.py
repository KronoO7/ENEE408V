import cv2
import threading
import queue
from picamera2 import Picamera2
from ultralytics import YOLO

# Initialize the Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (720, 720)  # Increased resolution for better detection
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Load the YOLOv8 model
model = YOLO("/home/team_usa/enee408v/vision/best (2).pt")
model.fuse()

threshold = 0.55
frame_queue = queue.Queue(maxsize=1)  # Queue with maxsize=1 to always get the latest frame

def process_frame(frame):
    results = model(frame)

    # Filter detections based on threshold
    valid_boxes = [box for box in results[0].boxes if box.conf >= threshold]

    # Create a new frame with filtered detections; Green: (0, 255, 0), purple: (162, 94, 142),
    annotated_frame = frame.copy()
    for box in valid_boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{box.cls[0]} {box.conf[0]:.2f}"
        cv2.putText(annotated_frame, 'Testudo', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Update the frame in the queue
    try:
        frame_queue.put(annotated_frame, block=False)
    except queue.Full:
        try:
            frame_queue.get_nowait()  # Discard the old frame
            frame_queue.put(annotated_frame, block=False)
        except queue.Empty:
            pass

def capture_and_process():
    while True:
        frame = picam2.capture_array()
        process_frame(frame)

# Start capturing and processing frames in a separate thread
capture_thread = threading.Thread(target=capture_and_process)
capture_thread.daemon = True
capture_thread.start()

# Main thread: Display the frames
try:
    while True:
        try:
            annotated_frame = frame_queue.get(timeout=1)
            cv2.imwrite("testudo.jpg", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except queue.Empty:
            continue
finally:
    picam2.stop()
    cv2.destroyAllWindows()
