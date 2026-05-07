import cv2

def mean_filter(image):
    output = cv2.blur(image, (5, 5))
    return output