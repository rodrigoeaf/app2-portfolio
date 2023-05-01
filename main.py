import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rodrigo Freitas")
    content = "Hi, I am Rodrigo! I am a Python student. todo todo todo todo todo."

    st.info(content)

content2 = """
Below you can find some apps I have built in Python! Fell free to contact me!
"""

st.write(content2)