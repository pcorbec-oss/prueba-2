import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Demo - dashboard3")

# Generar algunos datos de ejemplo
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "Ventas": [120, 150, 90, 200, 175],
    "Clientes": [30, 45, 20, 50, 40]
}
df = pd.DataFrame(data)

st.subheader("Tabla de datos")
st.dataframe(df)

st.subheader("Gráfico de barras de ventas")
fig = px.bar(df, x="Mes", y="Ventas", text="Ventas", color="Mes")
st.plotly_chart(fig)

st.subheader("Gráfico de líneas de clientes")
fig2 = px.line(df, x="Mes", y="Clientes", markers=True)
st.plotly_chart(fig2)
