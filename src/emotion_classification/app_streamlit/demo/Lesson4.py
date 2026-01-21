import streamlit as st

st.title("Lesson 4: WIDGET TƯƠNG TÁC")

st.subheader('1. Button')

if st.button("Bấm vào tôi: "):  # tra ve true 1 lan khi duoc an, reset khi co tuong tac vs widget khac
    st.write('Bạn vừa bấm nút!')
else:
    st.warning('Bạn quên bấm nút rồi!')

st.subheader("2. st.checkbox()")  # checkbox duoc giu lai khi rerun
agree = st.checkbox("Tôi đồng ý với điều khoản")
if agree:
    st.success("Cảm ơn bạn đã đồng ý!")
else:
    st.warning("Bạn chưa đồng ý!")
    

# duoc giu lai khi rerun
st.subheader("3. radio") 
genre = st.radio('Chọn thể loại yêu thích: ', ['Action', 'Romantic', 'Anime', 'Game'])
st.write(f"Bạn đã tích: {genre}")

st.subheader("4. dropdown")
language = st.selectbox("Chọn ngôn ngữ lập trình yêu thích", ["Python", "C++", "Java", "JavaScript"])
st.write(f"Bạn đã chọn: {language}")

st.subheader("5. multiselex")
foods = st.multiselect(
    'Chọn đồ ăn yêu thích: ',
    ['Phở', 'Bún bò', 'Bánh mỳ', 'Cơm tấm', 'Gỏi cuốn']
)

# st.write(f"Bạn đã chọn: {foods}")

if foods:
    st.success(f"Bạn đã chọn: {', '.join(foods)}")
else:
    st.warning('Bạn chưa chọn món nào!')
    

