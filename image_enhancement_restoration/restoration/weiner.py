import cv2
from scipy.signal import wiener
def wiener_filter(image):
    output = wiener(image)
    output = output.astype('uint8')
    return output