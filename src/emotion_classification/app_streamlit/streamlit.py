import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
import time

# --- ĐOẠN CODE CHỈ ĐƯỜNG ---
# Lấy đường dẫn hiện tại của file này
current_dir = os.path.dirname(os.path.abspath(__file__))

# Lấy đường dẫn thư mục cha (thư mục emotion_classification)
parent_dir = os.path.dirname(current_dir)

# Thêm vào hệ thống để Python tìm thấy thư mục 'model'
sys.path.append(parent_dir)
# ---------------------------

from model.load_model import load_model_from_drive
from model.load_model import process


try:
    model = load_model_from_drive()
    st.write("Model đã sẵn sàng sử dụng!")
    file = st.file_uploader("Chọn file ảnh", type=['jpg'])
    if not (file is None):
        # Xu ly file anh, chuan hoa, chuyen thanh tensor
        tensor = process(file)
        result = model.predict(tensor)
        
        class_id = np.argmax(result) 
        st.write(f"Kết quả phân loại: {class_id}")
        
except Exception as e:
    st.error(f"Lỗi khi load model: {e}")