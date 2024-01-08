import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of Cats")

col1,col2 = st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("./cat1.jpeg",caption="Persion Cat",width=300,use_column_width=True)
  st.write("Persian cats are cute and nice")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./cat2.jpeg",caption="Ragdoll Cat",width=300,use_column_width=True)
  st.write("Ragdoll cats are white in colour")
