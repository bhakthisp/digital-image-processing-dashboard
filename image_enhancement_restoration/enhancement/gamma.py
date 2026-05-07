import numpy as np

def gamma_correction(image, gamma=1.5):
    normalized = image / 255.0
    gamma_corrected = np.power(normalized, gamma)
    output = np.uint8(gamma_corrected * 255)
    return output