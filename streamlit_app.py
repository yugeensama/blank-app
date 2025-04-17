import streamlit as st
from datetime import datetime
import time
import requests
from PIL import Image
from io import BytesIO

# Configuración de página
st.set_page_config(
    page_title="Reloj Tenneco",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
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
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    
    .main-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        width: 100vw;
        background-color: #000;
    }
    
    .logo-container {
        margin-bottom: 30px;
    }
    
    .clock-container {
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }
    
    .time-block {
        background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
        border-radius: 15px;
        padding: 20px 30px;
        box-shadow: 0 0 20px rgba(0, 86, 179, 0.5);
        text-align: center;
        min-width: 150px;
        border: 2px solid var(--tenneco-blue);
    }
    
    .time-value {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        font-weight: 700;
        color: var(--tenneco-red);
        text-shadow: 0 0 15px rgba(227, 25, 55, 0.8);
        line-height: 1;
    }
    
    .time-label {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        color: #ffffff;
        margin-top: 10px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    
    .date-display {
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        color: var(--tenneco-blue);
        letter-spacing: 3px;
        margin-top: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def load_tenneco_logo():
    try:
        # URL alternativa del logo por si la oficial falla
        logo_url = "https://www.tenneco.com/themes/tenneco/images/logo.png"
        response = requests.get(logo_url, timeout=5)
        image = Image.open(BytesIO(response.content))
        return image
    except:
        try:
            # Intento con logo local si está en el repositorio
            image = Image.open("tenneco-logo.png")
            return image
        except:
            return None

# Mostrar el logo
logo = load_tenneco_logo()

# Contenedor principal
main_container = st.empty()

# Función para actualizar el reloj
def update_clock():
    now = datetime.now()
    
    # Formatear la hora y fecha
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")
    hours, minutes, seconds = current_time.split(":")
    
    # HTML del reloj
    clock_html = f"""
    <div class="main-container">
        <div class="logo-container">
            {f'<img src="{logo_url}" width="300">' if logo else '<h1 style="color: var(--tenneco-blue);">TENNECO</h1>'}
        </div>
        <div class="clock-container">
            <div class="time-block">
                <div class="time-value">{hours}</div>
                <div class="time-label">HORAS</div>
            </div>
            <div class="time-block">
                <div class="time-value">{minutes}</div>
                <div class="time-label">MINUTOS</div>
            </div>
            <div class="time-block">
                <div class="time-value">{seconds}</div>
                <div class="time-label">SEGUNDOS</div>
            </div>
        </div>
        <div class="date-display">{current_date}</div>
    </div>
    """
    
    # Mostrar el reloj
    main_container.markdown(clock_html, unsafe_allow_html=True)

# Actualizar cada segundo usando la caché de Streamlit
if st.button('Reiniciar'):
    st.experimental_rerun()

# Configurar el auto-refresh
update_clock()
time.sleep(1)
st.experimental_rerun()
