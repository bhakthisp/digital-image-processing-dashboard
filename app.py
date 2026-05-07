import streamlit as st
import cv2
import numpy as np

from processing.enhancement.negative import negative_transform
from processing.enhancement.log_transform import log_transform
from processing.enhancement.gamma import gamma_correction
from processing.enhancement.contrast import contrast_stretching

from processing.filters.mean import mean_filter
from processing.filters.median import median_filter
from processing.filters.gaussian import gaussian_filter
from processing.filters.sharpen import sharpen_filter

from processing.restoration.denoise import denoise_image
from processing.restoration.deblur import deblur_image
from processing.restoration.weiner import wiener_filter

st.set_page_config(page_title="Image Enhancement & Restoration", layout="wide")

st.title("Image Enhancement & Restoration")

st.sidebar.header("Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload an Image",
    type=["jpg", "png", "jpeg"]
)

category = st.sidebar.selectbox(
    "Select Category",
    ["Enhancement", "Filters", "Restoration"],
    key="sidebar_category"
)

if uploaded_file:
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
                st.image(
                    output,
                    channels="BGR",
                    width=520
                )