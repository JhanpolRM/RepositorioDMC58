import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Jhanpol Rosales M.")

st.sidebar.image("Image20260512194104.png")

sesion = st.sidebar.selectbox("Seleccione una Sesión", ["Sesión 01", "Sesión 02", "Sesión 03", "Sesión 04"])

if sesion == "Sesión 01":
  st.write("Bienvenido a la sesión 01")
  st.image("Image20260512194055.png")
  
elif sesion=="Sesión 02":
  st.write("Bienvenido a la sesión 02")
elif sesion=="Sesión 03":
  st.write("Bienvenido a la sesión 03")
else
  st.write("Bienvenido a la sesión 04")

