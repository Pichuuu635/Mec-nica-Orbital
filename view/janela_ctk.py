import customtkinter as ctk
import settings

janela = ctk.CTk()
janela.geometry(settings.GEOMETRY)
janela.configure(bg="#000000")
janela.after(1, lambda: janela.state("zoomed"))

def janela_init():
    janela.mainloop()