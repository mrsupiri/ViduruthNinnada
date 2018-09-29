import numpy as np
import cv2
import screeninfo

file = []
height = 1920
width = 1080


def play():
    screen = screeninfo.get_monitors()[1]
    window_name = 'video_frame'
    while True:
        try:
            cap = cv2.VideoCapture(file[-1])

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
        except Exception as e:
            image = np.zeros((height, width), dtype=np.float32)
            image[0, 0] = 0  # top-left corner
            image[height - 2, 0] = 0  # bottom-left
            image[0, width - 2] = 0  # top-right
            image[height - 2, width - 2] = 0  # bottom-rig
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                                  cv2.WINDOW_FULLSCREEN)
            cv2.imshow(window_name, image)
            # print(e)
