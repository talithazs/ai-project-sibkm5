import streamlit as st

st.set_page_config(
    page_title="Amazon Reviews for Sentiment Analysis",
    page_icon="img/mzn.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.image("img/ath2.png")

col1, col2, col3 = st.columns(3)
col2.title('Group Athena 2')
col2.write('AI Coach = Abdulghoffar Lugas Aga P. S.Si')
st.image('img/athena1.png')
st.image('img/athena2.png')
st.image('img/athena3.png')