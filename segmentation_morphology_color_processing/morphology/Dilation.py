import cv2
import numpy as np

def dilation(image):

    kernel = np.ones((5,5), np.uint8)

    output = cv2.dilate(
        image,
        kernel,
        iterations=1
    )

    return output