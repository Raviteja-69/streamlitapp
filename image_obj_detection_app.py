import streamlit as st
import PIL

from ultralytics import YOLO

# st.write("Hello, World!")
model_path = https://github.com/Raviteja-69/streamlitapp/blob/main/yolov8n.pt'

st.set_page_config(
    page_title='Object Detection using YOLOV8',
    page_icon='🤖',
    layout='wide',
    initial_sidebar_state='expanded'
)

# creating sidebar

with st.sidebar:
    st.header("Image/Video")
    source_img = st.sidebar.file_uploader(
        "Choose an Image...",type=("jpg","jpeg","png","bmp","webp"))

    # model options
    confidence = float(st.slider(
               "Select Model Confidence",25,100,40))/100

st.title("Object Detection using YOLOV8")

col1, col2 = st.columns(2)

with col1:
    if source_img:
        uploaded_image = PIL.Image.open(source_img)
        st.image(uploaded_image,
                 caption="Uploaded Image",
                 use_column_width=True
                 )
try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model. check the specified path: {model_path}")
    st.error(ex)

if st.sidebar.button('Detect Objects'):
    res = model.predict(uploaded_image, conf = confidence)
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]
    with col2:
        st.image(res_plotted, caption='Detected Image',
                 use_column_width=True)
