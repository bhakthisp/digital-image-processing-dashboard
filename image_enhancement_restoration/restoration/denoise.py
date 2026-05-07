import cv2
def denoise_image(image):
    output = cv2.fastNlMeansDenoisingColored(
        image,
        None,
        10,
        10,
        7,
        21
    )
    return output