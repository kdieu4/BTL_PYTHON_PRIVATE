import streamlit as st

side = st.sidebar
side.title("Tùy chọn")
option = side.selectbox(
    "Chọn một mục", 
    ["Trang chủ", "Giới thiệu", "Liên hệ"]
)
st.header(f"Bạn đã chọn: {option}")

if option == "Trang chủ":
    # col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.header("Cột 1")
        st.write("Nội dung bên trái")
    
    with col2:
        st.header("Cột 2")
        st.write("Nội dung ở giữa")
        
    with col3:
        st.header("Cột 3")
        st.write("Nội dung bên phải")
        
if option == "Giới thiệu":
    with st.expander("Xem thêm chi tiết: "):
        st.write("Đây là phần nội dung được ẩn mặc định")
        st.image('https://via.placeholder.com/150')