import streamlit as st
from projects.vision_pixtral_mistral.utils import analyze_image

def run():
    st.title("Vision with Pixtral 12B")
    st.write("""
    Our Pixtral 12B introduces vision capabilities, allowing it to analyze images 
    and provide insights based on visual content in addition to text. This multimodal 
    approach enables applications requiring both textual and visual understanding.
    """)

    # Input for Image URL
    image_url = st.text_input("Enter the URL of the image")

    if st.button("Analyze Image"):
        if image_url.strip():
            with st.spinner("Analyzing image..."):
                try:
                    result = analyze_image(image_url)
                    st.subheader("Image Analysis Result")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid image URL.")

