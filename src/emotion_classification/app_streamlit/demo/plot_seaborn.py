import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def sea_plot(df, cols):
    fig, ax = plt.subplots()
    sns.lineplot(
        df, 
        x = 'Age', # mặc định là cột Age
        y = cols[0],
        linewidth = 2,
        linestyle = '--',
        marker = '+'
    )
    
    ax.set_title('Biểu đồ với seaborn')
    st.pyplot(fig)