

# Librerias
import time  # para simular el tiempo real, bucle de tiempo
import numpy as np  # np significa "numpy" para cálculos numéricos
import pandas as pd  # para leer CSV y manipulación de DataFrames
import plotly.express as px  # gráficos interactivos
import streamlit as st  # desarrollo de aplicaciones web de datos 🎈

# Configuración de la página
st.set_page_config(
    page_title="Panel de Control de Ciencia de Datos en Tiempo Real",
    page_icon="✅",
    layout="wide",
)

# URL del conjunto de datos en formato CSV
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"


# Función para obtener los datos desde la URL del conjunto de datos
@st.cache_data  # Utiliza caché para evitar cargar los datos repetidamente
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)


df = get_data()  # Carga los datos en un DataFrame

# Título del panel de control
st.title("Panel de Control de Ciencia de Datos en Tiempo Real / Vivo")

# Filtros de nivel superior
job_filter = st.selectbox("Seleccionar el Trabajo", pd.unique(df["job"]))

# Creando un contenedor con un solo elemento
placeholder = st.empty()

# Filtrado del DataFrame
df = df[df["job"] == job_filter]

# Simulación de datos en tiempo real cercano / en vivo
for seconds in range(200):  # Bucle para simular 200 unidades de tiempo

    # Generación de datos simulados para "age_new" y "balance_new"
    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

    # Cálculo de Indicadores Clave de Rendimiento (KPIs) simulados
    avg_age = np.mean(df["age_new"])

    count_married = int(
        df[(df["marital"] == "married")]["marital"].count()
        + np.random.choice(range(1, 30))
    )

    balance = np.mean(df["balance_new"])

    # Actualización dinámica de la interfaz dentro del contenedor
    with placeholder.container():
        # Creación de tres columnas para los KPIs
        kpi1, kpi2, kpi3 = st.columns(3)

        # Mostrar los KPIs en las columnas respectivas
        kpi1.metric(
            label="Edad ⏳",
            value=round(avg_age),
            delta=round(avg_age) - 10,
        )

        kpi2.metric(
            label="Cantidad de Casados 💍",
            value=int(count_married),
            delta=-10 + count_married,
        )

        kpi3.metric(
            label="Saldo de Cuenta ＄",
            value=f"$ {round(balance, 2)} ",
            delta=-round(balance / count_married) * 100,
        )

        # Creación de dos columnas para los gráficos
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Primer Gráfico")
            fig = px.density_heatmap(
                data_frame=df, y="age_new", x="marital"
            )
            st.write(fig)

        with fig_col2:
            st.markdown("### Segundo Gráfico")
            fig2 = px.histogram(data_frame=df, x="age_new")
            st.write(fig2)

        st.markdown("### Vista Detallada de Datos")
        st.dataframe(df)
        time.sleep(1)  # Simula la actualización en tiempo real
