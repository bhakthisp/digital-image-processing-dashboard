import cv2

def thresholding(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, output = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    return output