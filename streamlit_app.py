import streamlit as st
from datetime import datetime
import time
import requests
from PIL import Image
from io import BytesIO

# Configurar la página para modo pantalla completa
st.set_page_config(layout="wide")

# Función para cargar el logo de Tenneco
def load_tenneco_logo():
    try:
        # URL del logo de Tenneco
        logo_url = "https://www.tenneco.com/wp-content/uploads/2019/10/tenneco-logo.png"
        response = requests.get(logo_url)
        image = Image.open(BytesIO(response.content))
        return image
    except:
        return None

# Función para calcular el tiempo transcurrido
def calculate_time_passed(start_date):
    now = datetime.now()
    delta = now - start_date
    
    total_seconds = delta.total_seconds()
    seconds = int(total_seconds % 60)
    minutes = int((total_seconds // 60) % 60)
    hours = int((total_seconds // 3600) % 24)
    days = delta.days % 30  # Aproximación
    months = delta.days // 30 % 12
    years = delta.days // 365
    
    return years, months, days, hours, minutes, seconds

# Mostrar el logo de Tenneco
logo = load_tenneco_logo()
if logo:
    st.image(logo, width=300)
else:
    st.title("Tenneco Time Counter")

# Fecha de referencia (puedes cambiarla)
reference_date = datetime(2000, 1, 1)  # 1 de Enero del 2000

# Crear placeholders para los contadores
year_ph = st.empty()
month_ph = st.empty()
day_ph = st.empty()
hour_ph = st.empty()
minute_ph = st.empty()
second_ph = st.empty()

# Estilo CSS para hacer los números grandes
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
    font-weight: bold;
    text-align: center;
    color: white;
    background-color: black;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Bucle para actualizar el contador
while True:
    years, months, days, hours, minutes, seconds = calculate_time_passed(reference_date)
    
    # Actualizar los placeholders con los nuevos valores
    year_ph.markdown(f"<p class='big-font'>Años: {years}</p>", unsafe_allow_html=True)
    month_ph.markdown(f"<p class='big-font'>Meses: {months}</p>", unsafe_allow_html=True)
    day_ph.markdown(f"<p class='big-font'>Días: {days}</p>", unsafe_allow_html=True)
    hour_ph.markdown(f"<p class='big-font'>Horas: {hours}</p>", unsafe_allow_html=True)
    minute_ph.markdown(f"<p class='big-font'>Minutos: {minutes}</p>", unsafe_allow_html=True)
    second_ph.markdown(f"<p class='big-font'>Segundos: {seconds}</p>", unsafe_allow_html=True)
    
    # Esperar 1 segundo antes de la próxima actualización
    time.sleep(1)
