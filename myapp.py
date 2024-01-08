import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of Cats")

col1,col2,col3,col4 = st.columns(4)
with col1:
  st.subheader("Persian Cat")
  st.image("./cat1.jpeg",caption="Persion Cat",width=500,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./cat2.jpeg",caption="Ragdoll Cat",width=500,use_column_width=True)
  st.write("Ragdoll cats are white in colour")
with col3:
  st.subheader("House Cat")
  st.image("./cat3.jpeg",caption="house Cat",width=500,use_column_width=True)
  st.write("house cats are very calm")
with col4:
  st.subheader("Random Cat")
  st.image("./cat4.jpeg",caption="Random Cat",width=500,use_column_width=True)
  st.write("Random cats are different in nature")
  
