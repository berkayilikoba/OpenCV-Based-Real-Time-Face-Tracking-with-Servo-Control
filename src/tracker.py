import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

face_center_x = None
face_center_y = None
radius = 25

last_x = None
last_y = None
alpha = 0.25

def detect_face(frame):
    global last_x, last_y

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    boxes = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(20,20))

    if len(boxes) == 0:
        return frame, None, None

    boxes = sorted(boxes, key=lambda b: b[2] * b[3], reverse=True)
    x, y, w, h = boxes[0]

    cx = (x + x + w) / 2
    cy = (y + y + h) / 2

    if last_x is None:
        last_x, last_y = cx, cy
    else:
        last_x = alpha * cx + (1 - alpha) * last_x
        last_y = alpha * cy + (1 - alpha) * last_y

    cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv.circle(frame, (int(last_x), int(last_y)), 6, (0,255,0), -1)

    return frame, last_x, last_y

def get_distance(frame):
    resized_frame = cv.resize(frame, (640,480))
    faced_frame, f_center_x, f_center_y = detect_face(resized_frame)
    height, width = faced_frame.shape[:2]
    cam_center_x = int(width / 2)

    distance_x = None

    if f_center_x is not None:
        distance_x = int(cam_center_x - f_center_x)
        cv.putText(faced_frame, f"Distance : {distance_x}", (40, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 0), 2)
    else:
        cv.putText(faced_frame, "No face detected", (40, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 2)

    cv.circle(faced_frame, (cam_center_x, int(height / 2)), 25, (0, 0, 255), 2)

    return faced_frame, distance_x

def is_inside(frame, distance, threshold = 25):
    if distance is None:
        return False

    if abs(distance) <= threshold:
        text = "INSIDE"
        colour = (0,255,0)
        inside = True
    else:
        text = "OUTSIDE"
        colour = (0,0,255)
        inside = False

    cv.putText(frame, text, (50, 150),
               cv.FONT_HERSHEY_SIMPLEX, 1.4, colour, 3)

    return inside
