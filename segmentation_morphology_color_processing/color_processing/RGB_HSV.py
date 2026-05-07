import cv2

def rgb_to_hsv(image):

    output = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )

    return output