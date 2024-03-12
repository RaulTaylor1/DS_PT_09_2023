import streamlit as st
from PIL import Image

imagen = Image.open(r'C:\Users\taylo\Documents\GitHub\DS_PT_09_2023\Data_Engineer\Streamlit\Teoria\img\591e3af95df3c.jpg')

st.image(imagen)