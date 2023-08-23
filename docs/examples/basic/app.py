import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# Título de la aplicación
st.title('Análisis de Datos con Streamlit')

# Cargar los datos (por ejemplo, un conjunto de datos sobre ventas)
data = pd.read_csv('https://raw.githubusercontent.com/fralfaro/Streamlit-Examples/main/docs/examples/basic/data.csv')

# Sidebar para opciones de filtrado
st.sidebar.header('Opciones de Filtrado')
selected_category = st.sidebar.selectbox('Seleccionar Categoría', data['category'].unique())

# Filtrar datos por categoría seleccionada
filtered_data = data[data['category'] == selected_category]

# Mostrar los datos filtrados en una tabla
st.subheader('Datos Filtrados')
st.write(filtered_data)

# Mostrar histograma de precios
st.subheader('Histograma de Precios')
fig, ax = plt.subplots()
hist_values, hist_bins = np.histogram(filtered_data['price'], bins=20)
plt.bar(hist_bins[:-1], hist_values, width=hist_bins[1] - hist_bins[0], color='blue', alpha=0.7)
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
st.pyplot(fig)

# Mostrar gráfico de dispersión entre precio y cantidad
st.subheader('Gráfico de Dispersión')
fig, ax = plt.subplots()
plt.scatter(filtered_data['price'], filtered_data['quantity'], alpha=0.5, color='green')
plt.xlabel('Precio')
plt.ylabel('Cantidad')
st.pyplot(fig)

# Mostrar resumen estadístico
st.subheader('Resumen Estadístico')
st.write(filtered_data.describe())

# Agregar una nota final
st.markdown('¡Explora y analiza los datos utilizando las opciones y gráficos anteriores!')
