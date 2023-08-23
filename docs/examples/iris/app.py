# Librerias
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image  # Importar la clase Image de la biblioteca Python Imaging Library (PIL)

# Cargar el conjunto de datos Iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_name'] = iris.target_names[iris.target]

# Cargar imágenes de flores Iris
setosa_image = Image.open('images/setosa.jpg')  # Asegúrate de tener las imágenes en la misma ubicación que este archivo
versicolor_image = Image.open('images/versicolor.jpg')
virginica_image = Image.open('images/virginica.jpg')


# Cargar el conjunto de datos Iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_name'] = iris.target_names[iris.target]



# Título de la aplicación
st.title('Explorador de Datos Iris')

# Encabezado
st.header('Conjunto de Datos Iris')

# Mostrar una tabla con los primeros registros del conjunto de datos
st.write(iris_df.head())

# Mostrar imágenes de las flores Iris en una fila
st.subheader('Imágenes de Flores Iris')
col1, col2, col3 = st.columns(3)  # Dividir el espacio horizontal en tres columnas

# Mostrar las imágenes en las columnas
with col1:
    st.image(setosa_image, caption='Iris Setosa', width=200)

with col2:
    st.image(versicolor_image, caption='Iris Versicolor',  width=200)

with col3:
    st.image(virginica_image, caption='Iris Virginica', width=200)


# Histograma interactivo de las características
st.subheader('Histograma de Características')
feature = st.selectbox('Seleccione una característica:', iris.feature_names)
plt.figure()
sns.histplot(iris_df[feature], bins=30, kde=True)
st.pyplot(plt)

# Gráfico interactivo de dispersión
st.subheader('Gráfico de Dispersión')
x_axis = st.selectbox('Seleccione una característica para el eje X:', iris.feature_names)
y_axis = st.selectbox('Seleccione una característica para el eje Y:', iris.feature_names)
plt.figure()
sns.scatterplot(data=iris_df, x=x_axis, y=y_axis, hue='target_name', palette='viridis')
st.pyplot(plt)

# Información sobre los tipos de flores Iris
st.subheader('Información de las Flores Iris')
flower_id = st.slider('Seleccione un ID de flor:', 0, len(iris.target_names)-1)
st.write('Nombre de la flor:', iris.target_names[flower_id])
st.write('Cantidad de muestras:', (iris.target == flower_id).sum())

# Mostrar el conjunto de datos completo si se desea
if st.checkbox('Mostrar Conjunto de Datos Completo'):
    st.write(iris_df)

# Pie de página
st.write('Hecho con Streamlit por Ejemplo')
