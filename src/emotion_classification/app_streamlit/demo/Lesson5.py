import streamlit as st
import numpy as np
import pandas as pd

file_uploader = st.file_uploader('Tải lên csv file: ', type=['csv'])

if file_uploader is not None:
    try: 
        df = pd.read_csv(file_uploader)
        st.success('Tải lên thành công')
        st.write("Dữ liệu của bạn")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi đọc file {e}!")
    
else:
    st.info('Vui lòng tải file csv để bắt đầu')
    