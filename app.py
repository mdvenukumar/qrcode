# pip install pyqrcode
# pip install pypng
import streamlit as st 
import pyqrcode
from PIL import Image
import io

# Set Streamlit page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon=":bar_chart:",
    layout="wide"
)

# Function to generate QR code and return the PNG stream
def generate_qr_code(url, scale=4):
    qr_code = pyqrcode.create(url)
    img_stream = io.BytesIO()
    qr_code.png(img_stream, scale=scale)
    st.image(Image.open(img_stream), width=300, caption="QR Code Preview")
    return img_stream

# Page layout
st.title("QR Code Generator")
st.markdown("### Convert your URL into a QR Code")

# User input and QR code generation
user_input = st.text_input("Enter URL", key="input")
if user_input:
    if st.button("Generate and Download QR Code (PNG)", key="generate_button"):
        if len(user_input) > 0:
            img_stream = generate_qr_code(user_input, scale=10)  # Adjust the scale value as needed
            st.download_button(
                label="Download QR Code (PNG)",
                data=img_stream.getvalue(),
                file_name="qr_code.png",
                key="download_button_png"
            )
        else:
            st.warning("Please enter a valid URL.")

# Description
st.sidebar.title("About")
st.sidebar.info(
    "This is a simple QR Code Generator built with Streamlit. "
    "Enter a URL, click the button, and download the generated QR Code."
)
st.sidebar.title("Follow the Creator")

# Social Icons
st.sidebar.markdown(
    """
    <div class="social-icons">
        <a href="https://www.instagram.com/_the_vk.__/" target="_blank" class="social-icon">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111421.png" alt="Instagram" style="width:24px;height:24px;">
        </a>
        &nbsp &nbsp
        <a href="https://www.linkedin.com/in/venukumarmd/" target="_blank" class="social-icon">
            <img src="https://cdn-icons-png.flaticon.com/128/1384/1384889.png" alt="LinkedIn" style="width:24px;height:24px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Additional styling
st.markdown(
    """
    <style>
        .st-bw {
            background-color: #1f1f1f;
        }
        .st-bv {
            padding: 0 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(
    """
    <div style="position: fixed; bottom: 5%; left: 2%; background-color: #bdebff; padding: 8px; border-radius: 5px; color: black; font-weight:bold";>
        THEVK
    </div>
    """,
    unsafe_allow_html=True
)
