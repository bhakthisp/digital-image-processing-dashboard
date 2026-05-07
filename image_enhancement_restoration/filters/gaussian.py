import cv2

def gaussian_filter(image):
    output = cv2.GaussianBlur(image, (5, 5), 0)
    return output