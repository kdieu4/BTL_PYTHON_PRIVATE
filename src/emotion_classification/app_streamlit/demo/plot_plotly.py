import plotly.express as px
import streamlit as st

def plotly(df, cols):
    fig3 = px.line(
        df.reset_index(),
        x='index',
        y=cols[0],
        markers=True,
        title="Biểu đồ với plotly"
    )
    st.plotly_chart(fig3, use_container_width=True)