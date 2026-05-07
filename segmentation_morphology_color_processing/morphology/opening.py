import cv2
import numpy as np

def opening(image):

    kernel = np.ones((5,5), np.uint8)

    output = cv2.morphologyEx(
        image,
        cv2.MORPH_OPEN,
        kernel
    )

    return output