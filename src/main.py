import cv2 as cv
import numpy as np
from tracker import *
import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

def set_servo_angle(angle):
    angle = max(0, min(180, angle))
    arduino.write(f"{int(angle)}\n".encode())

servo_x = 90
radius = 40
max_step = 2.0
sweep_step = 1.5
sweep_direction = 1

cap = cv.VideoCapture(2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    faced, distance_x = get_distance(frame)

    if distance_x is not None:

        if abs(distance_x) > radius:
            step_x = np.clip(distance_x, -radius, radius) / radius * max_step
            servo_x += step_x
            servo_x = max(0, min(180, servo_x))

        set_servo_angle(servo_x)
        sweep_direction = 1

    else:
        servo_x += sweep_step * sweep_direction
        if servo_x >= 180:
            servo_x = 180
            sweep_direction = -1
        elif servo_x <= 0:
            servo_x = 0
            sweep_direction = 1
        set_servo_angle(servo_x)
        cv.putText(faced, "Searching for face...", (40, 100),
           cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)


    cv.imshow("Face Detection", faced)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
