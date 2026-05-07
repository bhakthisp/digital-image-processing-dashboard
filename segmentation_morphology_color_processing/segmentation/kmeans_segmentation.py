import cv2
import numpy as np

def kmeans_segmentation(image):

    data = image.reshape((-1, 3))

    data = np.float32(data)

    criteria = (
        cv2.TERM_CRITERIA_EPS +
        cv2.TERM_CRITERIA_MAX_ITER,
        10,
        1.0
    )

    k = 4

    _, labels, centers = cv2.kmeans(
        data,
        k,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)

    segmented = centers[labels.flatten()]

    output = segmented.reshape(image.shape)

    return output