# Streamlit

## Introducción 

[Streamlit](https://streamlit.io/)  es una biblioteca de Python que ha revolucionado la forma en que los científicos de datos y desarrolladores pueden crear aplicaciones web interactivas con facilidad. A diferencia de las complejas herramientas de desarrollo web tradicionales, Streamlit se centra en la simplicidad y la eficiencia, permitiéndote convertir rápidamente tus análisis de datos, visualizaciones y modelos en aplicaciones web dinámicas y atractivas.

### ¿Por qué Streamlit es Especial?

1. **Sencillez y Velocidad:** Streamlit está diseñado para ser tan fácil como escribir un script de Python. No necesitas conocimientos profundos de HTML, CSS o JavaScript. En su lugar, puedes aprovechar tu conocimiento existente de Python para crear aplicaciones web.

2. **Interactividad en Tiempo Real:** Con unas pocas líneas de código, puedes agregar widgets interactivos como sliders, botones y checkboxes a tu aplicación. Estos elementos se actualizan en tiempo real según las interacciones del usuario, lo que brinda una experiencia interactiva y fluida.

3. **Integración con Bibliotecas de Visualización:** Streamlit se integra perfectamente con bibliotecas populares de visualización de datos como Matplotlib, Plotly y Altair. Puedes crear gráficos y visualizaciones interactivas directamente en tu aplicación.

4. **Widgets Predefinidos:** Streamlit ofrece una amplia variedad de widgets predefinidos que puedes usar para recopilar entradas del usuario y ajustar los parámetros de tus análisis y visualizaciones.

5. **Despliegue Fácil:** Una vez que hayas creado tu aplicación con Streamlit, desplegarla en la web es sencillo. Puedes usar plataformas en la nube como Heroku, AWS, o incluso Streamlit Sharing para compartir tu trabajo con otros.

6. **Caching Inteligente:** Streamlit tiene una función de caché integrada que te permite almacenar en caché resultados de cálculos costosos. Esto mejora el rendimiento de la aplicación al evitar que se recalculen los mismos resultados una y otra vez.

7. **Documentación Completa y Comunidad Activa:** Streamlit cuenta con una documentación detallada y una comunidad activa de usuarios que están dispuestos a ayudar y compartir ejemplos y consejos.


## Primeros Pasos

### Instalación

Para comenzar a utilizar Streamlit, primero necesitas instalarlo. Puedes instalarlo utilizando pip:

```bash
pip install streamlit
```

### Crear tu Primera Aplicación

Una vez instalado, puedes crear tu primera aplicación en unos pocos pasos sencillos:

1. **Importa la Biblioteca:**
   Importa la biblioteca Streamlit al comienzo de tu script de Python:

   ```python
   import streamlit as st
   ```

2. **Script Sencillo:**
   Utiliza las diversas funciones proporcionadas por Streamlit para crear elementos interactivos, como títulos, gráficos, sliders y más. Por ejemplo:

   ```python
   import streamlit as st
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt

   # Título de la aplicación
   st.title('Análisis de Datos con Streamlit')

   # Cargar los datos (por ejemplo, un conjunto de datos sobre ventas)
   data = pd.read_csv('data.csv')

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
   ```

3. **Ejecuta la Aplicación:**
   Ejecuta tu script de Python en la línea de comandos:

   ```bash
   streamlit run app.py
   ```

4. **Visualiza tu Aplicación:**
   Una vez que ejecutes el comando, se abrirá una ventana en tu navegador con la aplicación que creaste.


> **Nota**: más ejemplos de Streamlit en la siguiente [carpeta](examples).