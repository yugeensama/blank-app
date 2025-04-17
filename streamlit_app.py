import tkinter as tk
from tkinter import font
from datetime import datetime
import requests
from PIL import Image, ImageTk
from io import BytesIO

class TennecoClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj Tenneco")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        
        # Fecha de inicio para el contador (cámbiala)
        self.start_date = datetime(2020, 1, 1)
        
        # Configurar fuente
        self.big_font = font.Font(family='Arial', size=80, weight='bold')
        self.medium_font = font.Font(family='Arial', size=40)
        self.small_font = font.Font(family='Arial', size=20)
        
        # Cargar logo
        self.load_logo()
        
        # Crear widgets
        self.create_widgets()
        
        # Iniciar actualización
        self.update_clock()
    
    def load_logo(self):
        try:
            logo_url = "https://www.tenneco.com/themes/tenneco/images/logo.png"
            response = requests.get(logo_url, timeout=5)
            image = Image.open(BytesIO(response.content))
            
            # Redimensionar
            screen_width = self.root.winfo_screenwidth()
            new_width = screen_width // 4
            aspect_ratio = image.width / image.height
            new_height = int(new_width / aspect_ratio)
            image = image.resize((new_width, new_height), Image.LANCZOS)
            
            self.logo_img = ImageTk.PhotoImage(image)
            self.logo_label = tk.Label(self.root, image=self.logo_img, bg='black')
            self.logo_label.pack(pady=20)
        except:
            # Si falla, mostrar texto
            self.logo_label = tk.Label(self.root, text="TENNECO", 
                                      font=('Arial', 50, 'bold'), 
                                      fg='#0056b3', bg='black')
            self.logo_label.pack(pady=50)
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True)
        
        # Frame para el reloj
        clock_frame = tk.Frame(main_frame, bg='black')
        clock_frame.pack(pady=20)
        
        # Etiquetas del reloj
        self.time_labels = {
            'hours': tk.Label(clock_frame, text="00", font=self.big_font, 
                             fg='#e31937', bg='black'),
            'sep1': tk.Label(clock_frame, text=":", font=self.big_font, 
                           fg='white', bg='black'),
            'minutes': tk.Label(clock_frame, text="00", font=self.big_font, 
                              fg='#e31937', bg='black'),
            'sep2': tk.Label(clock_frame, text=":", font=self.big_font, 
                           fg='white', bg='black'),
            'seconds': tk.Label(clock_frame, text="00", font=self.big_font, 
                              fg='#e31937', bg='black')
        }
        
        # Posicionar reloj
        self.time_labels['hours'].grid(row=0, column=0)
        self.time_labels['sep1'].grid(row=0, column=1, padx=5)
        self.time_labels['minutes'].grid(row=0, column=2)
        self.time_labels['sep2'].grid(row=0, column=3, padx=5)
        self.time_labels['seconds'].grid(row=0, column=4)
        
        # Etiquetas descriptivas
        tk.Label(clock_frame, text="Horas", font=self.small_font, 
                fg='white', bg='black').grid(row=1, column=0)
        tk.Label(clock_frame, text="Minutos", font=self.small_font, 
                fg='white', bg='black').grid(row=1, column=2)
        tk.Label(clock_frame, text="Segundos", font=self.small_font, 
                fg='white', bg='black').grid(row=1, column=4)
        
        # Contador de días
        days_frame = tk.Frame(main_frame, bg='black')
        days_frame.pack(pady=30)
        
        self.days_label = tk.Label(days_frame, text="0", font=self.big_font, 
                                 fg='#e31937', bg='black')
        self.days_label.pack()
        
        tk.Label(days_frame, text=f"DÍAS DESDE {self.start_date.strftime('%d/%m/%Y')}", 
                font=self.small_font, fg='white', bg='black').pack()
        
        # Fecha actual
        self.date_label = tk.Label(main_frame, text="", font=self.medium_font, 
                                 fg='#0056b3', bg='black')
        self.date_label.pack(pady=20)
        
        # Botón de salida
        exit_button = tk.Button(self.root, text="Salir (ESC)", font=self.small_font, 
                               command=self.root.destroy, bg='red', fg='white')
        exit_button.pack(pady=20)
        
        # Configurar tecla ESC para salir
        self.root.bind('<Escape>', lambda e: self.root.destroy())
    
    def calculate_days(self):
        return (datetime.now() - self.start_date).days
    
    def update_clock(self):
        now = datetime.now()
        
        # Actualizar reloj
        self.time_labels['hours'].config(text=now.strftime("%H"))
        self.time_labels['minutes'].config(text=now.strftime("%M"))
        self.time_labels['seconds'].config(text=now.strftime("%S"))
        
        # Actualizar contador de días
        self.days_label.config(text=self.calculate_days())
        
        # Actualizar fecha
        self.date_label.config(text=now.strftime("%A, %d %B %Y"))
        
        # Programar próxima actualización
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = TennecoClock(root)
    root.mainloop()
