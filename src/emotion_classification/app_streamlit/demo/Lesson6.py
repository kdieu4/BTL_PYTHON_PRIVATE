import streamlit as st
import numpy as np
import pandas as pd
from get_df import get_df_plot
from plot_matplotlib import mat_plot
from plot_seaborn import sea_plot
from plot_plotly import plotly

st.title("Thực hành trực quan hóa dữ liệu với Streamlit")
st.subheader('Tải dữ liệu: ')

file_uploader = st.file_uploader(
    'Tải lên file csv: ',
    type=['csv']
)

if file_uploader is not None:
    try:
        df = pd.read_csv(file_uploader)
        st.success("Đã tải dữ liệu thành công!")
        # Ve 1 phan du lieu
        df_plot = get_df_plot(df)  # 50 dong dau, 10 cot dau

        st.subheader("1. Khám phá dữ liệu")

        st.markdown("**a. In ra 5 dòng đầu**")
        st.dataframe(df_plot.head())

        st.markdown("**b. Thống kê mô tả**")
        st.write(df_plot.describe())

        # Lay danh sach cac cot can ve
        cols = df_plot.columns

        # chon cac cot muon ve (st.multiselect)
        selects = st.multiselect(
            'Chọn đặc trưng',
            cols
        )

        # Ve bieu do
        st.subheader("2. Vẽ biểu đồ với st.line_chart")
        if selects:
            st.line_chart(df_plot[selects])
        else:
            st.warning('Vui lòng chọn cột để vẽ')

        st.subheader("3. Vẽ biểu đồ với Matplotlib")
        if selects:
            mat_plot(df_plot, selects)
        else:
            st.warning('Vui lòng chọn cột để vẽ')

        st.subheader("4. Vẽ biểu đồ với Seaborn")
        if selects:
            sea_plot(df_plot, selects)
        else:
            st.warning('Vui lòng chọn cột để vẽ')

        st.subheader("5. Vẽ biểu đồ với Plotly")
        if selects:
            plotly(df_plot, selects)
        else:
            st.warning('Vui lòng chọn cột để vẽ')

    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi đọc file! {e}")
else:
    st.info("Vui lòng tải file csv để bắt đầu!")
