import customtkinter as ctk
import settings
from PIL import Image
from view import janela_ctk
from view.janela_ctk import janela, janela_init
from view.input_data import input_data_init

def play_init():
    
    global frame_play
    
    frame_play = ctk.CTkFrame(janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BG_DARK)
    frame_play.pack(fill="both", expand=True)
    
    label_titulo = ctk.CTkLabel(frame_play, text="APOGEE", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 70, "bold"))
    label_titulo.place(relx=0.5, rely=0.1, anchor="center")
    
    label_sub = ctk.CTkLabel(frame_play, text="Aerospace Mission & Trajectory Simulator", text_color=settings.COLOR_TEXT_MAIN,font=(settings.FONT_FAMILY_TECH, 18, "italic"))
    label_sub.place(relx=0.5, rely=0.18, anchor="center")
    
    try:
        img_data = Image.open("view/rocket.png") # Caminho da sua imagem
        img_foguete = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(600, 337))
        
        label_img = ctk.CTkLabel(frame_play, width=100, height=200, image=img_foguete, text="", bg_color="transparent", fg_color="transparent")
        label_img.place(relx=0.5, rely=0.45, anchor="center")
    except:
        print("Imagem não encontrada, pulando...")
        
    button_start = ctk.CTkButton(frame_play, text="START", font=(settings.FONT_FAMILY_TECH, 16, "bold"), text_color="white", fg_color=settings.COLOR_ACCENT, hover_color="#14375e", corner_radius=10, height=50, width=400, command=start)
    button_start.place(relx=0.5, rely=0.8, anchor="center")
    
    label_versao = ctk.CTkLabel(frame_play, text="v1.0.0", font=("Arial", 15))
    label_versao.place(relx=0.95, rely=0.97, anchor="e")
    
    
    janela_init()
    
def start():
    frame_play.destroy()
    input_data_init()