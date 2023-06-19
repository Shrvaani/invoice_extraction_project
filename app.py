# image_extraction.py

import streamlit as st
from PIL import Image
import pytesseract
from datetime import datetime

@st.cache
def load_image(image_file):
    return Image.open(image_file)

def extract_data_from_image(image):
    # Preprocess the image
    processed_image = image.convert("L")  # Convert to grayscale
    processed_image = processed_image.point(lambda x: 0 if x < 200 else 255, "1")  # Thresholding

    # Extract text from the image
    text = pytesseract.image_to_string(processed_image)

    # Process the extracted text if needed
    # ...

    return text

def main():
    st.title("Image Data Extraction")
    
    # Upload the image file
    uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = load_image(uploaded_image)
        
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract data from the image
        extracted_data = extract_data_from_image(image)

        # Display the extracted data
        st.subheader("Extracted Data")
        st.text(extracted_data)

if __name__ == "__main__":
    main()
