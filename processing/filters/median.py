import cv2

def median_filter(image):
    output = cv2.medianBlur(image, 5)
    return output