import cv2
def negative_transform(image):
    negative = 255 - image
    return negative