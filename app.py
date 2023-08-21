import streamlit as st
from rembg import remove
from PIL import Image

st.title("Remove Background")
col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Load Image", accept_multiple_files =True)
if images:
    for image in images:
        with Image.open(image) as img:
            col1.header("Original")
            col1.image(img)

            output = remove(img)
            col2.header("Extracted")
            col2.image(output)
            with open(f"{output}.png", "rb") as file:
                btn = st.download_button(
                        label="Download image",
                        data=file,
                        file_name="flower.png",
                        mime="image/png"
                      )
