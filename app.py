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
  precio=st.number_input("Ingrese el precio del producto", min_value=0, max_value=5000, value=2)
  descuento=st.number_input("Ingrese el descuento del producto (0-100%)", min_value=0, max_value=100)
  precio_final_producto=precio - (precio*(descuento/100))
  st.write("El precio final del producto es:", precio_final_producto)


elif sesion=="Sesión 03":
  st.write("Bienvenido a la sesión 03")
else:
  st.write("Bienvenido a la sesión 04")

