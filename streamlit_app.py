import streamlit as st
from datetime import datetime
import requests
from PIL import Image
from io import BytesIO

# Configuración de página
st.set_page_config(
    page_title="Reloj Tenneco",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargar logo
def load_tenneco_logo():
    try:
        logo_url = "https://www.tenneco.com/themes/tenneco/images/logo.png"
        response = requests.get(logo_url, timeout=5)
        image = Image.open(BytesIO(response.content))
        return image
    except:
        try:
            return Image.open("tenneco-logo.png")
        except:
            return None

logo = load_tenneco_logo()

# Mostrar logo
if logo:
    st.image(logo, width=300)
else:
    st.title("TENNECO")

# Refrescar cada segundo
st_autorefresh = st.experimental_rerun if not hasattr(st, 'autorefresh') else st.autorefresh
st_autorefresh(interval=1000, key="refresh")

# Obtener fecha y hora actual
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%A, %d %B %Y")

# Días desde una fecha fija
start_date = datetime(2024, 1, 1)
days_elapsed = (now - start_date).days

# Mostrar información
st.markdown("## ⏰ Reloj Actual")
st.write(f"**Hora actual:** {current_time}")
st.write(f"**Fecha actual:** {current_date}")
st.write(f"**Días desde el 1 de enero de 2024:** {days_elapsed}")

# Botón para reiniciar manualmente
if st.button("Reiniciar"):
    st.experimental_rerun()
