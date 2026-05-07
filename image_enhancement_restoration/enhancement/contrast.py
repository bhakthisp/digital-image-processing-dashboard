import cv2
def contrast_stretching(image):
    min_val = image.min()
    max_val = image.max()
    stretched = ((image - min_val) / (max_val - min_val)) * 255
    return stretched.astype('uint8')