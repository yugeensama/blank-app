import streamlit as st

# 🟢 Esto debe ir al principio
st.set_page_config(page_title="Contador Tenneco", layout="wide")

from datetime import datetime
from dateutil.relativedelta import relativedelta
from streamlit_autorefresh import st_autorefresh

# Auto-refresh cada segundo
st_autorefresh(interval=1000, key="contadorrefresh")

# Estilos CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0f1117;
        color: #ffffff;
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 50px;
    }
    .logo-container img {
        max-height: 200px;
        height: auto;
        width: auto;
    }
    .contador-container {
        display: flex;
        justify-content: center;
        gap: 80px;
        flex-wrap: wrap;
        margin-top: 3rem;
    }
    .bloque {
        background-color: #1e222d;
        padding: 60px;
        border-radius: 30px;
        box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
        text-align: center;
        min-width: 180px;
    }
    .valor {
        font-size: 100px;
        font-weight: bold;
        color: #2ecc71;
    }
    .etiqueta {
        font-size: 30px;
        color: #bbbbbb;
        margin-top: 15px;
    }
    .mensaje {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Mostrar el logo centrado y sin estirarse
st.markdown("""
    <div class="logo-container">
        <img src="tenneco-logo-freelogovectors.net_.png" alt="Tenneco Logo">
    </div>
""", unsafe_allow_html=True)

# Fecha de inicio
fecha_inicio = datetime(2022, 5, 10, 8, 0, 0)
ahora = datetime.now()
diferencia = relativedelta(ahora, fecha_inicio)

# Extraer tiempo
años = diferencia.years
meses = diferencia.months
días = diferencia.days
horas = diferencia.hours
minutos = diferencia.minutes
segundos = diferencia.seconds

# Mostrar bloques
st.markdown(f"""
<div class="contador-container">
    <div class="bloque">
        <div class="valor">{años}</div>
        <div class="etiqueta">AÑOS</div>
    </div>
    <div class="bloque">
        <div class="valor">{meses}</div>
        <div class="etiqueta">MESES</div>
    </div>
    <div class="bloque">
        <div class="valor">{días}</div>
        <div class="etiqueta">DÍAS</div>
    </div>
    <div class="bloque">
        <div class="valor">{horas}</div>
        <div class="etiqueta">HORAS</div>
    </div>
    <div class="bloque">
        <div class="valor">{minutos}</div>
        <div class="etiqueta">MINUTOS</div>
    </div>
    <div class="bloque">
        <div class="valor">{segundos}</div>
        <div class="etiqueta">SEGUNDOS</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Frase final
st.markdown("""
    <div class="mensaje">
        Sin accidentes reportables
    </div>
""", unsafe_allow_html=True)
