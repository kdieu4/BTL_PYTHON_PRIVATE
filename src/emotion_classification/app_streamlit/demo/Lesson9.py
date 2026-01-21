import streamlit as st

st.title('Demo session_state')
st.markdown('---')

col_1, col_2 = st.columns(2)
count = 0

with col_1:
    st.subheader("Khong dung sesson state")
    if st.button('count'):
        count += 1
    
    st.write(f'Gia tri hien tai: {count}')
    
with col_2:
    st.subheader('Dung session state')
    if 'count' not in st.session_state:
        st.session_state.count = 0
        
    col_2_1, col_2_2 = col_2.columns(2)
    
    with col_2_1:
        if st.button('Increase'):
            st.session_state.count += 1
    
    with col_2_2:
        if st.button('Reset'):
            st.session_state.count = 0
    
    st.write(f'Gia tri hien tai: {st.session_state.count}')    