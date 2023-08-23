import streamlit as st
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# Título de la aplicación
st.title('Ejemplo sencillo con Streamlit')

# Cargar un conjunto de datos de ejemplo (Iris)
iris = datasets.load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Mostrar los primeros registros del conjunto de datos
st.subheader('Primeros registros del conjunto de datos:')
st.dataframe(iris_data.head())

# Mostrar descripción estadística del conjunto de datos
st.subheader('Descripción estadística del conjunto de datos:')
st.write(iris_data.describe())

# Mostrar gráfico simple por columna
st.subheader('Gráficos por columna:')
for feature_name in iris.feature_names:
    st.subheader(f'Gráfico de {feature_name}')
    fig, ax = plt.subplots()
    ax.hist(iris_data[feature_name], bins=20)
    st.pyplot(fig)

# Pie de página
st.subheader('¡Fin del ejemplo!')
st.write('Gracias por usar Streamlit.')