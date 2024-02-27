import pytesseract
from PIL import Image
import streamlit as st


# reads the text from the image using pillow and pytesseract
def read_text_from_image(image_path):
    img = Image.open(image_path)
    # img = img.convert('L')
    text = pytesseract.image_to_string(img)
    return text.replace('www.kenhub.com', '').replace('KEN', '').replace('\n\n\n\n aT', '').strip()


# create user interface for image upload
st.title("Image to Text")
uploaded_files = st.file_uploader(
    "Upload image(s)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()

    st.write(read_text_from_image(uploaded_file))
