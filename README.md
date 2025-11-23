# OpenCV-Based-Real-Time-Face-Tracking-with-Servo-Control
A real-time face tracking system that uses OpenCV for detection and a servo motor for dynamic camera alignment. This project performs real-time face tracking using OpenCV and controls a servo motor based on the X-coordinate of the detected face. If no face is detected, the servo performs a scanning motion. The servo is controlled via Arduino.

---

## Features

- Real-time face detection using Haar Cascade
- Servo motor movement based on face center (X-axis)
- Servo performs scanning if no face is detected
- Arduino-based servo control
- Simple Python and OpenCV implementation

---

## Requirements

- Python 3.x
- OpenCV
- Numpy
- PySerial
- Arduino (with connected servo motor)

Install the required Python packages:

```bash
pip install opencv-python numpy pyserial
````

---

## File Structure

```
project/
│
├── tracker.py      # Face detection and distance calculation functions
├── main.py         # Main loop for camera and servo control
└── README.md
```

---

## Usage

1. Connect Arduino to your computer and attach the servo motor to the appropriate pin (e.g., D9).
2. Update the serial port in `main.py` if needed:

```python
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
```

3. Connect a camera to your computer and run:

```bash
python main.py
```

4. When a face is detected, the servo follows the face. If no face is detected, the servo performs scanning.
5. Press `q` to exit the program.

---

## Parameters

* `radius`: Defines the X-axis distance threshold for servo adjustment.
* `max_step`: Maximum angle change per frame.
* `sweep_step`: Step size when scanning.
* `alpha`: Smoothing factor for face center tracking.

---

## License

This project is open-source and free to use.

