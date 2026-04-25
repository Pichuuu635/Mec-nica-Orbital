import customtkinter as ctk
import settings

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry(settings.GEOMETRY)
janela.configure(fg_color=settings.COLOR_BG_DARK, bg=settings.COLOR_BG_DARK)
janela.after(1, lambda: janela.state("zoomed"))

def janela_init():
    janela.mainloop()