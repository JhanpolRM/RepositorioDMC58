import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones as lf


st.set_page_config(page_title="Proyecto Ejemplo Streamlit", page_icon="🐍")

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Jhanpol Rosales M.")

st.sidebar.image("Image20260512194104.png")

sesion = st.sidebar.selectbox("Seleccione una Sesión", ["Sesión 01", "Sesión 02", "Sesión 03", "Sesión 04", "Sesión 05"])

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
  fin_rango=st.slider("Seleccione un valor", min_value=0, max_value=20, value=7)
  arreglo=np.arange(0, fin_rango)
  st.write(arreglo)

elif sesion=="Sesión 04":
  st.write("Bienvenido la sesión 4")
  archivo = st.sidebar.file_uploader("Cargue su archivo")
  
  if archivo is not None:
    
    if archivo.name.endswith(".csv"):
      datos = pd.read_csv(archivo)
    elif archivo.name.endswith(".xlsx"):
      datos = pd.read_excel(archivo)

    st.write(datos)

  else: 
    st.write("Cargue el archivo ")
  
 else:
   st.write("Bienvenido la sesión 5")
