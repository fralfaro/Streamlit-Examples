# Librerias
import streamlit as st  # Importa la biblioteca Streamlit para crear aplicaciones web interactivas
import pandas as pd  # Importa la biblioteca Pandas para manejar los datos
import numpy as np  # Importa la biblioteca NumPy para cálculos numéricos

# Establece el título de la aplicación
st.title('Recogidas de Uber en Nueva York')

# Define el nombre de la columna de fechas y horas en los datos
DATE_COLUMN = 'date/time'

# Define la URL del conjunto de datos en formato CSV
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Función que carga los datos desde la URL con caché
@st.cache_data  # Utiliza caché para acelerar el acceso a los datos
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)  # Lee el archivo CSV con un número máximo de filas
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)  # Convierte los nombres de columna a minúsculas
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])  # Convierte la columna de fechas/horas a formato datetime
    return data

# Muestra un mensaje de estado de carga de datos
data_load_state = st.text('Cargando datos...')

# Carga los datos y muestra un mensaje de estado cuando está hecho
data = load_data(10000)  # Carga los datos con un máximo de 10,000 filas
data_load_state.text("¡Listo! (usando st.cache_data)")

# Crea un checkbox para mostrar los datos en bruto
if st.checkbox('Mostrar datos en bruto'):
    st.subheader('Datos en bruto')
    st.write(data)  # Muestra los datos en forma tabular

# Muestra un subtítulo y un gráfico de barras con el número de recogidas por hora
st.subheader('Número de recogidas por hora')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)  # Muestra el gráfico de barras

# Slider para filtrar las recogidas por hora
hour_to_filter = st.slider('hora', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]  # Filtra los datos por la hora seleccionada

# Muestra un subtítulo y un mapa con las recogidas en la hora seleccionada
st.subheader('Mapa de todas las recogidas a las %s:00' % hour_to_filter)
st.map(filtered_data)  # Muestra un mapa interactivo con marcadores en las ubicaciones de las recogidas
