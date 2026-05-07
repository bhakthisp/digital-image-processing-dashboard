import cv2

def color_enhancement(image):

    output = cv2.detailEnhance(
        image,
        sigma_s=10,
        sigma_r=0.15
    )

    return output