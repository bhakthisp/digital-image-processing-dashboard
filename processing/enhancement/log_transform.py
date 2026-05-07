import cv2
import numpy as np

def log_transform(image):
    c = 255 / np.log(1 + np.max(image))
    log_image = c * np.log(1 + image)
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image