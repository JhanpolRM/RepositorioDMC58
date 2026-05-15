import streamlit as st
import numpy as np
import libreria_funciones as lf

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
  st.write("Bienvenido a la sesión 04")
  principal = st.number_input("Ingrese el monto del préstamo", value=1000)
  tasa_anual = st.number_input("Ingrese la tasa anual en decimal", value=0.1, min_value=0.0, max_value=1.0)
  anios = st.number_input("Ingrese el número de años del préstamo", value=1)
  pagos_anio = st.number_input("Ingrese la cantidad de pagos por año", value=12)
    
  cuota = round(lf.cuota_prestamo(principal, tasa_anual, anios, pagos_anio),2)
  st.write(f"El valor de la cuota es {cuota}")

else:
  st.write("Bienvenido a la sesión 05")


