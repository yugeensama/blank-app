import streamlit as st

# 🟢 ¡Esto debe ir primero!
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
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 120px;
        margin-bottom: 30px;
    }
    .contador-container {
        display: flex;
        justify-content: center;
        gap: 60px;
        flex-wrap: wrap;
        margin-top: 2rem;
    }
    .bloque {
        background-color: #1e222d;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
        text-align: center;
        min-width: 140px;
    }
    .valor {
        font-size: 70px;
        font-weight: bold;
        color: #2ecc71;
    }
    .etiqueta {
        font-size: 24px;
        color: #bbbbbb;
        margin-top: 10px;
    }
    .mensaje {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Logo Tenneco centrado
st.image("tenneco-logo-freelogovectors.net_.png")

# Fecha de inicio del contador
fecha_inicio = datetime(2022, 1, 25, 0, 0, 0)
ahora = datetime.now()
diferencia = relativedelta(ahora, fecha_inicio)
segundos_totales = int((ahora - fecha_inicio).total_seconds())

# Extraer los valores
años = diferencia.years
meses = diferencia.months
días = diferencia.days
horas = diferencia.hours
minutos = diferencia.minutes
segundos = diferencia.seconds

# Mostrar como bloques en columnas
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

# Frase debajo de los contadores
st.markdown("""
    <div class="mensaje">
        Sin accidentes reportables desde:
    </div>
""", unsafe_allow_html=True)
