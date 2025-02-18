# Importamos las librerias necesarias
import pandas as pd
import streamlit as st
import plotly.express as px

# Importamos los datos del DataSet a un DataFrame
car_data = pd.read_csv(r"C:\Users\Pc\OneDrive\Documentos\TripleTen\Sprint_7\proyecto_s7\datasets\vehicles_us.csv")

# Creamos un encabezado
st.header('Anuncios de venta de coches')

# Creamos un botón para graficar un histograma
hist_button = st.button('Construir histograma del kilometraje')

if hist_button: # Al hacer clic en el botón escribe un mensaje
    st.write('Creación de un histograma del kilometraje para el conjunto de datos de anuncios de venta de coches')
    #Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Creamos un botón para hacer un gráfico de dispersión
scatter_button = st.button('Construir un grafico de dispersión del kilometraje y el precio')

if scatter_button: # Al hacer clic en el botón escribe un mensaje
    st.write('Creación de un gráfico de dispersión del kilometraje y el precio para el conjunto de datos de anuncios de venta de coches')
    #Crear un gráfico de dispersión
    fig_1 = px.scatter(car_data, x="odometer", y="price")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)