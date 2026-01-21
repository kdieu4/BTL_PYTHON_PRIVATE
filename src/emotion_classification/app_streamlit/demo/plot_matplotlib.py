import matplotlib.pyplot as plt
import streamlit as st

def mat_plot(df, cols):
    fig, ax = plt.subplots()
    
    plt.plot(
        df.index,
        df[cols],
        marker = 'o',
        linestyle = '--',
        linewidth = 0.5
    )
    
    ax.set_title("Biểu đồ với matplotlib")
    st.pyplot(fig)