import streamlit as st
import numpy as np

# Título de la aplicación
st.title("Cheat Sheet de NumPy en Streamlit")

# Sección para la creación de arrays
st.header("Creación de Arrays")

st.subheader("Crear un array de ceros")
rows, cols = st.columns(2)
with rows:
    zero_rows = st.slider("Filas", min_value=1, max_value=10, value=1)
with cols:
    zero_cols = st.slider("Columnas", min_value=1, max_value=10, value=1)
zeros_array = np.zeros((zero_rows, zero_cols))
st.write(zeros_array)

# Sección para operaciones básicas
st.header("Operaciones Básicas")

st.subheader("Operaciones Matemáticas")
a = st.number_input("Ingrese el valor de 'a'", value=5.0)
b = st.number_input("Ingrese el valor de 'b'", value=3.0)
result_add = np.add(a, b)
result_sub = np.subtract(a, b)
result_mul = np.multiply(a, b)
result_div = np.divide(a, b)
st.write(f"a + b = {result_add}")
st.write(f"a - b = {result_sub}")
st.write(f"a * b = {result_mul}")
st.write(f"a / b = {result_div}")

# Sección para funciones estadísticas
st.header("Funciones Estadísticas")

values = st.text_input("Ingrese valores separados por comas (ejemplo: 2, 4, 6)", "2, 4, 6")
values_list = [float(val.strip()) for val in values.split(",")]
mean = np.mean(values_list)
median = np.median(values_list)
std_dev = np.std(values_list)
st.write(f"Valores ingresados: {values_list}")
st.write(f"Media: {mean}")
st.write(f"Mediana: {median}")
st.write(f"Desviación Estándar: {std_dev}")
