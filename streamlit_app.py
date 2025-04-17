import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
from streamlit_autorefresh import st_autorefresh

# Refresca cada 1000ms = 1 segundo
st_autorefresh(interval=1000, key="contadorrefresh")

# Configuración general
st.set_page_config(page_title="Contador Tenneco", layout="wide")

# Estilo CSS personalizado
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
        text-align: center;
        padding-top: 30px;
    }
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 150px;
    }
    .timer {
        font-size: 80px;
        font-weight: bold;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
st.image("tenneco_logo.png")

# Fecha inicial del contador (ajusta a tu gusto)
fecha_inicio = datetime(2022, 5, 10, 8, 0, 0)

# Calculamos la diferencia
ahora = datetime.now()
diferencia = relativedelta(ahora, fecha_inicio)

# Mostramos el contador
st.markdown(f"""
<div class="timer">
    {diferencia.years} años<br>
    {diferencia.months} meses<br>
    {diferencia.days} días<br>
    {diferencia.hours} horas
</div>
""", unsafe_allow_html=True)
