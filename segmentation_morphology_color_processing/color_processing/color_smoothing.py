import cv2

def color_smoothing(image):

    output = cv2.bilateralFilter(
        image,
        9,
        75,
        75
    )

    return output