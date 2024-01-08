
import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("<h3 style='color: Yellow,font-size: 60px;'>Types of Cats</h3>", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)
with col1:
  st.markdown("<h3 style='color: blue;'>Persian Cat</h3>", unsafe_allow_html=True)
  st.image("./cat1.jpeg",caption="Persion Cat",width=500,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.markdown("<h3 style='color: orange;'>Ragdoll Cat</h3>", unsafe_allow_html=True)
  st.image("./cat2.jpeg",caption="Ragdoll Cat",width=500,use_column_width=True)
  st.write("Ragdoll cats are white in colour")
with col3:
  st.markdown("<h3 style='color: red;'>House Cat</h3>", unsafe_allow_html=True)
  st.image("./cat3.jpeg",caption="house Cat",width=500,use_column_width=True)
  st.write("house cats are very calm")
with col4:
  st.markdown("<h3 style='color: green;'>Random Cat</h3>", unsafe_allow_html=True)
  st.image("./cat4.jpeg",caption="Random Cat",width=500,use_column_width=True)
  st.write("Random cats are different in nature")
  
