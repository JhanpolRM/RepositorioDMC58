import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Jhanpol Rosales M.")

sesion = st.sidebar.selectbox("Seleccione una Sesión", ["Sesión 01", "Sesión 02", "Sesión 03", "Sesión 04"])
