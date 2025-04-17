import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
from streamlit_autorefresh import st_autorefresh

# Configuración de página
st.set_page_config(page_title="Contador Tenneco", layout="wide")

# Refrescar cada segundo
st_autorefresh(interval=1000, key="auto-refresh")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f, #2e2e3e);
        color: #f0f0f0;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }

    .logo-container {
        margin-top: 30px;
        margin-bottom: 30px;
    }

    .contador {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }

    .bloque {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 0 20px rgba(0,0,0,0.4);
        min-width: 160px;
    }

    .valor {
        font-size: 64px;
        font-weight: 700;
        color: #4ade80;
    }

    .etiqueta {
        font-size: 20px;
        color: #cbd5e1;
        margin-top: 10px;
        letter-spacing: 1px;
    }

    .mensaje {
        margin-top: 60px;
        font-size: 28px;
        font-weight: bold;
        color: #facc15;
    }
    </style>
""", unsafe_allow_html=True)

# Centrado del logo con columnas
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("tenneco-logo-freelogovectors.net_.png", use_container_width=False, width=300)

# Calcular diferencia de tiempo
fecha_inicio = datetime(2022, 5, 10, 8, 0, 0)
ahora = datetime.now()
diferencia = relativedelta(ahora, fecha_inicio)

años = diferencia.years
meses = diferencia.months
días = diferencia.days
horas = diferencia.hours
minutos = diferencia.minutes
segundos = diferencia.seconds

# Mostrar contador en bloques
st.markdown(f"""
<div class="contador">
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
        <div class="valor">{horas:02d}</div>
        <div class="etiqueta">HORAS</div>
    </div>
    <div class="bloque">
        <div class="valor">{minutos:02d}</div>
        <div class="etiqueta">MINUTOS</div>
    </div>
    <div class="bloque">
        <div class="valor">{segundos:02d}</div>
        <div class="etiqueta">SEGUNDOS</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Mensaje inferior
st.markdown("""
    <div class="mensaje">
        Sin accidentes reportables
    </div>
""", unsafe_allow_html=True)
