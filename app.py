import streamlit as st
from rembg import remove
from PIL import Image
import io

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')



st.title("Remove Background")
st.divider()
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
            
            # Create a BytesIO object to store the image data
            output_stream = io.BytesIO()
            output.save(output_stream, format="PNG")
            
            # Download button
            v_spacer(height=3, sb=True)
            col2.download_button(
                label="Download image",
                data=output_stream.getvalue(),
                file_name="extracted_image.png",
                mime="image/png")
