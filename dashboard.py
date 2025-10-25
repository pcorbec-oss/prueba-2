import streamlit as st
import pandas as pd
import plotly.express as px

# Título del dashboard
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
st.title("Dashboard de Ventas con Streamlit y Plotly")

# Cargar datos de ejemplo
@st.cache_data
def cargar_datos():
    data = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "Canal": ["Online", "Tienda", "Online", "Tienda", "Online", "Tienda"],
        "Ventas": [12500, 9800, 14300, 11200, 15800, 13000],
        "Cantidad": [250, 190, 280, 230, 310, 260]
    }
    return pd.DataFrame(data)

df = cargar_datos()

# Filtros
st.sidebar.header("Filtros")
canal = st.sidebar.multiselect("Selecciona el canal", options=df["Canal"].unique(), default=df["Canal"].unique())

df_filtrado = df[df["Canal"].isin(canal)]

# Visualizaciones
col1, col2 = st.columns(2)

with col1:
    fig_ventas = px.bar(df_filtrado, x="Mes", y="Ventas", color="Canal", barmode="group", title="Ventas por Mes")
    st.plotly_chart(fig_ventas, use_container_width=True)

with col2:
    fig_cantidad = px.line(df_filtrado, x="Mes", y="Cantidad", color="Canal", markers=True, title="Cantidad Vendida por Mes")
    st.plotly_chart(fig_cantidad, use_container_width=True)

# Métricas generales
st.subheader("Resumen general")
col3, col4, col5 = st.columns(3)
col3.metric("Ventas Totales", f"${df_filtrado['Ventas'].sum():,.0f}")
col4.metric("Promedio por Mes", f"${df_filtrado['Ventas'].mean():,.0f}")
col5.metric("Unidades Vendidas", f"{df_filtrado['Cantidad'].sum():,.0f}")



