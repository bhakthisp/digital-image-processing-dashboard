import cv2
import numpy as np

def deblur_image(image):
    sharpen_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)
    output = cv2.filter2D(image, -1, sharpen_kernel)
    return output