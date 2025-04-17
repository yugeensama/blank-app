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
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 50px;
    }
    img {
        max-height: 200px;  /* Tamaño grande del logo */
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
        border-radius: 30px;  /* Aumento en bordes */
        box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
        text-align: center;
        min-width: 180px;  /* Aumento en el tamaño de los bloques */
    }
    .valor {
        font-size: 100px;  /* Aumento en el tamaño de los números */
        font-weight: bold;
        color: #2ecc71;
    }
    .etiqueta {
        font-size: 30px;  /* Aumento en el tamaño de la etiqueta */
        color: #bbbbbb;
        margin-top: 15px;
    }
    .mensaje {
        text-align: center;
        font-size: 36px;  /* Aumento en el tamaño de la frase */
        font-weight: bold;
        color: #ffffff;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Cargar y mostrar el logo
try:
    st.image("tenneco-logo-freelogovectors.net_.png", use_column_width=True)
except:
    st.error("No se pudo cargar el logo. Asegúrate de que la imagen esté en la carpeta correcta.")

# Fecha de inicio del contador
fecha_inicio = datetime(2022, 5, 10, 8, 0, 0)
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
        Sin accidentes reportables
    </div>
""", unsafe_allow_html=True)
