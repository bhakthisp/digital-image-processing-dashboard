import cv2
import numpy as np

def erosion(image):

    kernel = np.ones((5,5), np.uint8)

    output = cv2.erode(
        image,
        kernel,
        iterations=1
    )

    return output