import cv2
import imutils
import numpy as np

"""
Reference:
    - Resized image: https://pyimagesearch.com/2021/01/20/opencv-resize-image-cv2-resize/
    - python OpenCV ip camera: https://www.youtube.com/watch?v=JbHE1j0F8rk
"""


def resizeImage(image, width=500):
    resized = imutils.resize(image, width=width)
    return resized


url = "http://10.185.240.19:8080/video"
capture = cv2.VideoCapture(url)
success, frame = capture.read()

while success:
    success, frame = capture.read()
    resized = resizeImage(frame, width=800)
    cv2.imshow("IP Camera", resized)

    if cv2.waitKey(10) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
