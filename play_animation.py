# import numpy as np
import cv2
import screeninfo


def play(file):
    screen = screeninfo.get_monitors()[1]
    window_name = 'video_frame'
    while True:
        cap = cv2.VideoCapture(file)

        while cap.isOpened():
            ret, frame = cap.read()
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                                  cv2.WINDOW_FULLSCREEN)
            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()


play('/home/supiri/Videos/sample.mp4')
