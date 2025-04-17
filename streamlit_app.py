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
        font-family: Arial, sans-serif;
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
    
    .counter-container {
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }
    
    .time-block, .day-block {
        background: #1a1a1a;
        border-radius: 10px;
        padding: 20px 25px;
        box-shadow: 0 0 10px rgba(0, 86, 179, 0.3);
        text-align: center;
        min-width: 120px;
        border: 1px solid var(--tenneco-blue);
    }
    
    .time-value, .day-value {
        font-size: 3.5rem;
        font-weight: bold;
        color: var(--tenneco-red);
        line-height: 1;
    }
    
    .time-label, .day-label {
        font-size: 1.2rem;
        color: #ffffff;
        margin-top: 8px;
    }
    
    .date-display {
        font-size: 1.5rem;
        color: var(--tenneco-blue);
        margin-top: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def load_tenneco_logo():
    try:
        logo_url = "https://www.tenneco.com/themes/tenneco/images/logo.png"
        response = requests.get(logo_url, timeout=5)
        image = Image.open(BytesIO(response.content))
        return image
    except:
        try:
            image = Image.open("tenneco-logo.png")
            return image
        except:
            return None

# Fecha de inicio para el contador de días (cambia esta fecha)
START_DATE = datetime(2020, 1, 1)

def calculate_days():
    now = datetime.now()
    return (now - START_DATE).days

logo = load_tenneco_logo()
main_container = st.empty()

def update_display():
    now = datetime.now()
    days_passed = calculate_days()
    
    # Formatear la hora y fecha
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    hours, minutes, seconds = current_time.split(":")
    
    # HTML del display
    display_html = f"""
    <div class="main-container">
        <div class="logo-container">
            {f'<img src="https://www.tenneco.com/themes/tenneco/images/logo.png" width="250">' if logo else '<h1 style="color: var(--tenneco-blue);">Manu</h1>'}
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
        
        <div class="counter-container">
            <div class="day-block">
                <div class="day-value">{days_passed}</div>
                <div class="day-label">DÍAS DESDE</div>
                <div class="day-label">{START_DATE.strftime('%d/%m/%Y')}</div>
            </div>
        </div>
        
        <div class="date-display">Fecha actual: {current_date}</div>
    </div>
    """
    
    main_container.markdown(display_html, unsafe_allow_html=True)

# Configurar el auto-refresh
update_display()
time.sleep(1)
st.experimental_rerun()
