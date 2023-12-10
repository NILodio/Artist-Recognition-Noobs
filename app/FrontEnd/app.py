import streamlit as st
from PIL import Image
from utils import make_predictions

# Set page configuration
st.set_page_config(
    page_title='Artist Recognition',
    page_icon='😇'
)

st.title("Artist Recognition")
st.write("Upload an image, choose a model, and we'll predict the artist!")

file_upload = st.file_uploader("Choose a file", type=['jpg', 'png'])

selected_model = st.selectbox("Select Model", ["VGG19", "ResNet50"])

if file_upload and st.button("Make Predictions"):
    try:
        uploaded_image = Image.open(file_upload)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

        predictions = make_predictions(uploaded_image, selected_model)

        st.subheader("Predictions:")
        st.json(predictions)

    except Exception as e:
        st.error(f"Error: {str(e)}")

st.markdown("---")
st.write("Made with ❤️ by Python Noobs")

st.markdown(
    """
    <style>
        body {
            color: #333;
            background-color: #f8f9fa;
        }
        .st-ba {
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)
