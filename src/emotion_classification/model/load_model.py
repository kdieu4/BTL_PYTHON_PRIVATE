# load model, file weight tu drive xuong project
# muc tieu: moi lan nguoi dung chay chi load model 1 lan

import os
import gdown
import tensorflow as tf
import streamlit as st
import numpy as np
import cv2

# Hàm này sẽ chỉ chạy 1 lần duy nhất nhờ @st.cache_resource


@st.cache_resource
def load_model_from_drive():
    if not os.path.exists('model'):
        os.makedirs('model')

    model_path = 'model/my_mnist_model.keras'
    drive_file_id = '1_5xVOZZWp-SSDnGlDRN3dqfeBjrIEPWu'

    if not os.path.exists(model_path):
        with st.spinner('Đang tải model từ Google Drive...'):
            url = f'https://drive.google.com/uc?id={drive_file_id}'
            gdown.download(url, model_path, quiet=False)
            st.success('Tải model thành công!')

    model = tf.keras.models.load_model(model_path)
    return model


def process(file):
    file.seek(0)
    file_bytes = file.read()
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    if img is None:
        st.error("Lỗi: Không thể đọc được file ảnh.")
        return None

    st.image(img, caption="Ảnh gốc", channels="RGB")

    if img is None:
        return None, None

    # 2. Resize về 28x28
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)

    # 3. Chuẩn hóa
    img_array = (img.astype('float32') / 255.0) - 0.5
    img_array = img_array.reshape(1, 28, 28, 1)

    return img_array
