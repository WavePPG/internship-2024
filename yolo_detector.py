from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")


def draw_boxes(frame, boxes):
    """Draw detected bounding boxes on image frame"""

    # Create annotator object
    annotator = Annotator(frame)
    for box in boxes:
        if box.cls == 15:
            #class_id = box.cls 
            class_name = model.names[int(15)]
            coordinator = box.xyxy[0]
            confidence = box.conf
            # Draw bounding box
            annotator.box_label(
                box=coordinator, label=class_name, color=(200, 100, 0)
            )
    


    return annotator.result()


def detect_object(frame):
    """Detect object from image frame"""

    # Detect object from image frame
    results = model.predict(frame)

    for result in results:
        frame = draw_boxes(frame, result.boxes)
    

    return frame

#frame = draw_boxes(frame, result.boxes)
if __name__ == "__main__":
    video_path = "CatZoomies.mp4"
    cap = cv2.VideoCapture(video_path)

    # # Define the codec and create VideoWriter object
    # video_writer = cv2.VideoWriter(
    #     video_path + "_demo.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30, (1280, 720)
    # )

    while cap.isOpened():
        # Read image frame
        ret, frame = cap.read()

        if ret:
            # Detect motorcycle from image frame
            frame_result = detect_object(frame)
            #front and name
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(frame,  
                        'Adithep Thiabrit + Clicknext-Internship-2024',  
                        (550, 50),  
                        font, 1,  
                        (0, 0, 255),  
                        3,  
                        cv2.LINE_8) 
            # Write result to video
            # video_writer.write(frame_result)

            # Show result
            cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
            cv2.imshow("Video", frame_result)
            cv2.waitKey(30)

        else:
            break

    # Release the VideoCapture object and close the window
    # video_writer.release()
    cap.release()
    cv2.destroyAllWindows()
