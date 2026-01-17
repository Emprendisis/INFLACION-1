import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from banxico_client import BanxicoClient

SERIE = "SP30578"

@st.cache_data(ttl=3600)
def load_data():
    client = BanxicoClient()
    payload = client.get_series(SERIE)
    datos = payload["bmx"]["series"][0]["datos"]
    df = pd.DataFrame(datos)
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["dato"] = pd.to_numeric(df["dato"], errors="coerce")
    df = df.sort_values("fecha")
    return df

st.set_page_config(page_title="Inflación anual – Banxico", layout="wide")
st.title("Inflación anual (Banxico) – Serie SP30578")

df = load_data()

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Serie histórica")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("Último dato")
    last = df.dropna().iloc[-1]
    st.metric("Inflación anual (%)", f"{last['dato']:.2f}", delta=None)
    st.caption(f"Fecha: {last['fecha'].date()}")

st.subheader("Gráfica")
fig = plt.figure()
plt.plot(df["fecha"], df["dato"])
plt.xlabel("Fecha")
plt.ylabel("Inflación anual (%)")
st.pyplot(fig, clear_figure=True)
