import streamlit as st
import cv2
import numpy as np

from image_enhancement_restoration.enhancement.negative import negative_transform
from image_enhancement_restoration.enhancement.log_transform import log_transform
from image_enhancement_restoration.enhancement.gamma import gamma_correction
from image_enhancement_restoration.enhancement.contrast import contrast_stretching

from image_enhancement_restoration.filters.mean import mean_filter
from image_enhancement_restoration.filters.median import median_filter
from image_enhancement_restoration.filters.gaussian import gaussian_filter
from image_enhancement_restoration.filters.sharpen import sharpen_filter

from image_enhancement_restoration.restoration.denoise import denoise_image
from image_enhancement_restoration.restoration.deblur import deblur_image
from image_enhancement_restoration.restoration.weiner import wiener_filter

from segmentation_morphology_color_processing.segmentation.thresholding import thresholding
from segmentation_morphology_color_processing.segmentation.sobel_edge import sobel_edge
from segmentation_morphology_color_processing.segmentation.kmeans_segmentation import kmeans_segmentation
from segmentation_morphology_color_processing.morphology.errosion import erosion
from segmentation_morphology_color_processing.morphology.Dilation import dilation
from segmentation_morphology_color_processing.morphology.opening import opening
from segmentation_morphology_color_processing.morphology.closing import closing
from segmentation_morphology_color_processing.color_processing.RGB_HSV import rgb_to_hsv
from segmentation_morphology_color_processing.color_processing.color_enhancement import color_enhancement
from segmentation_morphology_color_processing.color_processing.color_smoothing import color_smoothing

st.set_page_config(page_title="Image Processing Dashboard", layout="wide")

st.title("Image Processing Dashboard")

st.sidebar.header("Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload an Image",
    type=["jpg", "png", "jpeg"]
)

main_module = st.sidebar.selectbox(
    "Select Main Module",
    ["Image Enhancement & Restoration", "Segmentation, Morphology & Color Processing"],
    key="sidebar_main_module"
)

if main_module == "Image Enhancement & Restoration":
    categories = ["Enhancement", "Filters", "Restoration"]
elif main_module == "Segmentation, Morphology & Color Processing":
    categories = ["Segmentation", "Morphology", "Color Processing"]

category = st.sidebar.selectbox(
    "Select Category",
    categories,
    key="sidebar_category"
)

if uploaded_file:
    if main_module == "Image Enhancement & Restoration":
        if category == "Enhancement":
            technique = st.sidebar.selectbox(
                "Select Technique",
                [
                    "Negative Transformation",
                    "Log Transformation",
                    "Gamma Correction",
                    "Contrast Stretching"
                ],
                key="sidebar_technique_enhancement"
            )
        elif category == "Filters":
            technique = st.sidebar.selectbox(
                "Select Technique",
                [
                    "Mean Filter",
                    "Median Filter",
                    "Gaussian Filter",
                    "Sharpen Filter"
                ],
                key="sidebar_technique_filters"
            )
        else:
            technique = st.sidebar.selectbox(
                "Select Technique",
                [
                    "Noise Removal",
                    "Deblurring",
                    "Wiener Filter"
                ],
                key="sidebar_technique_restoration"
            )
    elif main_module == "Segmentation, Morphology & Color Processing":
        if category == "Segmentation":
            technique = st.sidebar.selectbox(
                "Select Technique",
                ["Thresholding", "Sobel Edge Detection", "K-Means Segmentation"],
                key="sidebar_technique_segmentation"
            )
        elif category == "Morphology":
            technique = st.sidebar.selectbox(
                "Select Technique",
                ["Erosion", "Dilation", "Opening", "Closing"],
                key="sidebar_technique_morphology"
            )
        elif category == "Color Processing":
            technique = st.sidebar.selectbox(
                "Select Technique",
                ["RGB to HSV", "Color Enhancement", "Color Smoothing"],
                key="sidebar_technique_color"
            )
else:
    technique = None

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(file_bytes, 1)

    if image is None:
        st.error("Failed to load the image. Please upload a valid image file.")

    else:

        output = None

        if technique is not None:
            if main_module == "Image Enhancement & Restoration":
                if category == "Enhancement":

                    if technique == "Negative Transformation":
                        output = negative_transform(image)

                    elif technique == "Log Transformation":
                        output = log_transform(image)

                    elif technique == "Gamma Correction":
                        output = gamma_correction(image)

                    elif technique == "Contrast Stretching":
                        output = contrast_stretching(image)

                elif category == "Filters":

                    if technique == "Mean Filter":
                        output = mean_filter(image)

                    elif technique == "Median Filter":
                        output = median_filter(image)

                    elif technique == "Gaussian Filter":
                        output = gaussian_filter(image)

                    elif technique == "Sharpen Filter":
                        output = sharpen_filter(image)

                elif category == "Restoration":

                    if technique == "Noise Removal":
                        output = denoise_image(image)

                    elif technique == "Deblurring":
                        output = deblur_image(image)

                    elif technique == "Wiener Filter":
                        output = wiener_filter(image)

            elif main_module == "Segmentation, Morphology & Color Processing":
                if category == "Segmentation":

                    if technique == "Thresholding":
                        output = thresholding(image)

                    elif technique == "Sobel Edge Detection":
                        output = sobel_edge(image)

                    elif technique == "K-Means Segmentation":
                        output = kmeans_segmentation(image)

                elif category == "Morphology":

                    if technique == "Erosion":
                        output = erosion(image)

                    elif technique == "Dilation":
                        output = dilation(image)

                    elif technique == "Opening":
                        output = opening(image)

                    elif technique == "Closing":
                        output = closing(image)

                elif category == "Color Processing":

                    if technique == "RGB to HSV":
                        output = rgb_to_hsv(image)

                    elif technique == "Color Enhancement":
                        output = color_enhancement(image)

                    elif technique == "Color Smoothing":
                        output = color_smoothing(image)

            if output is not None and output.dtype != np.uint8:
                output = cv2.normalize(output, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        if output is not None:
            col1, spacer, col2 = st.columns([1, 0.08, 1])
            with col1:
                st.markdown("### Original Image")
                st.image(
                    image,
                    channels="BGR",
                    width=520
                )
            with spacer:
                st.write("")
            with col2:
                st.markdown("### Processed Image")
                if output.ndim == 2:
                    st.image(output, width=520)
                else:
                    st.image(output, channels="BGR", width=520)