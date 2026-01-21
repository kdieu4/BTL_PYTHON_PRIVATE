import streamlit as st

# 1. st.title("Relax Day with me") - Hien thi tieu de chinh
st.title("Relax - Thứ 4 ngày 21")
st.write('---')

# 2. st.header() - Hien thi tieu de cap 2
st.header("1. Học Streamlit 60 phút")
st.markdown("""
    #### Tự học Streamlit trong 60 phút!
    ##### *Nội dung buổi học*
    - Hiển thị text
    - Hiển thị dữ liệu:...
    - Cu phap co ban
            """)

st.code("""
    st.title("Đây là tiêu đề chính")
    st.text("Hien thi chu co ban")
    st.write("Hien thi chu da dang")
    st.markdown("Hien thi chu theo form setup")
    st.code("Hien thi code")
        """)

st.write("---")

st.header("2. Copy of Học Streamlit 60 phút")
st.markdown("""
    #### Tự học Streamlit trong 60 phút!
    ##### *Nội dung buổi học*
    - Hiển thị text
    - Hiển thị dữ liệu:...
    - Cú pháp cơ bản
            """)

st.code("""
    st.title("Đây là tiêu đề chính")
    st.text("Hiển thị chữ cơ bản")
    st.write("Hien thi chu da dang")
    st.markdown("Hien thi chu theo form setup")
    st.code("Hien thi code")
        """)

st.write("---")

st.markdown("[Link tới video hướng dẫn](https://www.youtube.com/watch?v=_8DWIzwUxz0&t=1989s)")

