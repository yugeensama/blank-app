import streamlit as st
from datetime import datetime
import time
import requests
from PIL import Image
from io import BytesIO

# Configurar la página para modo pantalla completa
st.set_page_config(layout="wide")

# Estilo CSS personalizado
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

:root {
    --tenneco-blue: #0056b3;
    --tenneco-red: #e31937;
    --tenneco-gray: #333333;
}

body {
    background-color: #000000;
    color: white;
    font-family: 'Orbitron', sans-serif;
}

.digital-clock {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #000000;
}

.tenneco-logo {
    margin-bottom: 2rem;
    max-width: 300px;
}

.time-container {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
}

.time-box {
    background: linear-gradient(145deg, #1a1a1a, #333333);
    border-radius: 15px;
    padding: 1.5rem 2rem;
    box-shadow: 0 10px 25px rgba(0, 86, 179, 0.3);
    text-align: center;
    min-width: 150px;
    border: 2px solid var(--tenneco-blue);
}

.time-value {
    font-size: 5rem;
    font-weight: 700;
    color: var(--tenneco-red);
    text-shadow: 0 0 10px rgba(227, 25, 55, 0.7);
    line-height: 1;
}

.time-label {
    font-size: 1.5rem;
    color: #ffffff;
    margin-top: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.date-display {
    font-size: 2rem;
    color: var(--tenneco-blue);
    margin-top: 2rem;
    letter-spacing: 3px;
}

.footer {
    position: fixed;
    bottom: 20px;
    width: 100%;
    text-align: center;
    font-size: 1rem;
    color: #666666;
}
</style>
""", unsafe_allow_html=True)

# Función para cargar el logo de Tenneco
def load_tenneco_logo():
    try:
        logo_url = "https://www.tenneco.com/wp-content/uploads/2019/10/tenneco-logo.png"
        response = requests.get(logo_url)
        image = Image.open(BytesIO(response.content))
        return image
    except:
        return None

# Función para formatear el tiempo con dos dígitos
def format_time(value):
    return f"{value:02d}"

# Mostrar el logo de Tenneco
logo = load_tenneco_logo()

# Contenedor principal
with st.container():
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown('<div class="digital-clock">', unsafe_allow_html=True)
        
        if logo:
            st.image(logo, width=300, output_format="PNG")
        else:
            st.markdown('<h1 style="text-align: center; color: var(--tenneco-blue);">TENNECO</h1>', unsafe_allow_html=True)
        
        # Placeholders para el reloj
        time_ph = st.empty()
        date_ph = st.empty()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Bucle principal para actualizar el reloj
while True:
    now = datetime.now()
    
    # Obtener componentes de fecha y hora
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")
    hours, minutes, seconds = current_time.split(":")
    
    # Crear el HTML para el reloj digital
    clock_html = f"""
    <div class="time-container">
        <div class="time-box">
            <div class="time-value">{hours}</div>
            <div class="time-label">Horas</div>
        </div>
        <div class="time-box">
            <div class="time-value">{minutes}</div>
            <div class="time-label">Minutos</div>
        </div>
        <div class="time-box">
            <div class="time-value">{seconds}</div>
            <div class="time-label">Segundos</div>
        </div>
    </div>
    """
    
    # Actualizar los placeholders
    time_ph.markdown(clock_html, unsafe_allow_html=True)
    date_ph.markdown(f'<div class="date-display">{current_date}</div>', unsafe_allow_html=True)
    
    # Esperar 1 segundo antes de la próxima actualización
    time.sleep(1)
