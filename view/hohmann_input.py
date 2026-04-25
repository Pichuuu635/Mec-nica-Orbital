import customtkinter as ctk
import settings
from view import janela_ctk
from view.janela_ctk import janela, janela_init
from tkinter import messagebox

def hohmann_input_init(dados_basicos, callback):
    frame_hohmann = ctk.CTkFrame(janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BG_DARK)
    frame_hohmann.pack(fill="both", expand=True)

    def make_entry(placeholder, relx, rely):
        entry = ctk.CTkEntry(frame_hohmann, width=250, height=37, placeholder_text=placeholder,
                             font=(settings.FONT_FAMILY_TECH, 15), fg_color=settings.COLOR_BG_CARD,
                             border_width=1, border_color=settings.COLOR_BORDER,
                             corner_radius=12, text_color=settings.COLOR_TEXT_MAIN)
        entry.place(relx=relx, rely=rely, anchor="center")
        return entry

    label_titulo = ctk.CTkLabel(frame_hohmann, text="DADOS DA TRANSFERÊNCIA DE HOHMANN:", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 50, "bold"))
    label_titulo.place(relx=0.5, rely=0.1, anchor="center")

    entry_orbita_inicial = make_entry("Órbita Inicial (km): ", 0.33, 0.25)
    label_orbita_inicial = ctk.CTkLabel(frame_hohmann, text="Altitude da órbita inicial. \n Exemplo: 200", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_orbita_inicial.place(relx=0.33, rely=0.32, anchor="center")

    entry_orbita_final = make_entry("Órbita Final (km): ", 0.67, 0.25)
    label_orbita_final = ctk.CTkLabel(frame_hohmann, text="Altitude da órbita final. \n Exemplo: 35786", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_orbita_final.place(relx=0.67, rely=0.32, anchor="center")

    entry_velocidade_inicial = make_entry("Velocidade Inicial (km/s): ", 0.33, 0.45)
    label_velocidade_inicial = ctk.CTkLabel(frame_hohmann, text="Velocidade na órbita inicial. \n Exemplo: 7.8", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_velocidade_inicial.place(relx=0.33, rely=0.52, anchor="center")

    entry_velocidade_final = make_entry("Velocidade Final (km/s): ", 0.67, 0.45)
    label_velocidade_final = ctk.CTkLabel(frame_hohmann, text="Velocidade na órbita final. \n Exemplo: 3.07", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_velocidade_final.place(relx=0.67, rely=0.52, anchor="center")

    entry_delta_v1 = make_entry("ΔV1 (km/s): ", 0.33, 0.65)
    label_delta_v1 = ctk.CTkLabel(frame_hohmann, text="Impulso para transferência. \n Exemplo: 2.4", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_delta_v1.place(relx=0.33, rely=0.72, anchor="center")

    entry_delta_v2 = make_entry("ΔV2 (km/s): ", 0.67, 0.65)
    label_delta_v2 = ctk.CTkLabel(frame_hohmann, text="Impulso para inserção. \n Exemplo: 1.5", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_delta_v2.place(relx=0.67, rely=0.72, anchor="center")

    def validate_hohmann(dados_hoh):
        errors = []
        for key, value in dados_hoh.items():
            if not value.strip():
                errors.append(f"{key}: Campo vazio.")
            else:
                try:
                    num = float(value)
                    if num < 0:
                        errors.append(f"{key}: Deve ser não-negativo.")
                except ValueError:
                    errors.append(f"{key}: Deve ser um número válido.")
        if errors:
            messagebox.showerror("Erro de Validação", "\n".join(errors))
            return False
        return True

    def simular():
        dados_hoh = {
            "orbita_inicial": entry_orbita_inicial.get(),
            "orbita_final": entry_orbita_final.get(),
            "velocidade_inicial": entry_velocidade_inicial.get(),
            "velocidade_final": entry_velocidade_final.get(),
            "delta_v1": entry_delta_v1.get(),
            "delta_v2": entry_delta_v2.get()
        }
        if validate_hohmann(dados_hoh):
            dados_basicos.update(dados_hoh)
            frame_hohmann.destroy()
            callback(dados_basicos)

    button_simular = ctk.CTkButton(frame_hohmann, text="SIMULAR", font=(settings.FONT_FAMILY_TECH, 16, "bold"), text_color="white", fg_color=settings.COLOR_ACCENT, hover_color="#14375e", corner_radius=10, height=50, width=400, command=simular)
    button_simular.place(relx=0.5, rely=0.9, anchor="center")