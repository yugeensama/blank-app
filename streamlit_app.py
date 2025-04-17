import streamlit as st
from datetime import datetime
import time
import requests
from PIL import Image
from io import BytesIO

# Configuración de la página
st.set_page_config(
    page_title="Reloj Tenneco",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Fecha de inicio para el contador (ajusta según necesites)
START_DATE = datetime(2020, 1, 1)

# Función para cargar el logo con manejo robusto de errores
def load_logo():
    try:
        # Intenta cargar desde URL
        logo_url = "https://www.tenneco.com/themes/tenneco/images/logo.png"
        response = requests.get(logo_url, timeout=3)
        response.raise_for_status()  # Lanza error si la solicitud falla
        return Image.open(BytesIO(response.content))
    except requests.RequestException:
        try:
            # Intenta cargar localmente si hay error
            return Image.open("tenneco-logo.png")
        except:
            return None

# Función para calcular días transcurridos
def calculate_days():
    return (datetime.now() - START_DATE).days

# Diseño principal
def main():
    logo = load_logo()
    
    # CSS personalizado
    st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: white;
            font-family: Arial, sans-serif;
        }
        .clock-display {
            font-size: 5rem;
            font-weight: bold;
            color: #e31937;
            text-align: center;
        }
        .day-counter {
            font-size: 3rem;
            color: #e31937;
            text-align: center;
            margin: 20px 0;
        }
        .date-display {
            font-size: 1.5rem;
            color: #0056b3;
            text-align: center;
        }
        .logo-container {
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Mostrar logo
    with st.container():
        if logo:
            st.image(logo, width=250)
        else:
            st.markdown("<h1 style='text-align: center; color: #0056b3;'>TENNECO</h1>", 
                       unsafe_allow_html=True)
    
    # Placeholders para la información dinámica
    time_placeholder = st.empty()
    day_placeholder = st.empty()
    date_placeholder = st.empty()
    
    # Bucle de actualización (usando session state)
    if 'last_update' not in st.session_state:
        st.session_state.last_update = time.time()
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    days_passed = calculate_days()
    current_date = now.strftime("%A, %d %B %Y")
    
    # Mostrar información
    time_placeholder.markdown(f"""
    <div class="clock-display">
        {current_time}
    </div>
    """, unsafe_allow_html=True)
    
    day_placeholder.markdown(f"""
    <div class="day-counter">
        {days_passed} días desde {START_DATE.strftime('%d/%m/%Y')}
    </div>
    """, unsafe_allow_html=True)
    
    date_placeholder.markdown(f"""
    <div class="date-display">
        {current_date}
    </div>
    """, unsafe_allow_html=True)
    
    # Forzar actualización cada segundo
    if time.time() - st.session_state.last_update > 1:
        st.session_state.last_update = time.time()
        st.experimental_rerun()

if __name__ == "__main__":
    main()
