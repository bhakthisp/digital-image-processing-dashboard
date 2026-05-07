import cv2
import numpy as np

def closing(image):

    kernel = np.ones((5,5), np.uint8)

    output = cv2.morphologyEx(
        image,
        cv2.MORPH_CLOSE,
        kernel
    )

    return output