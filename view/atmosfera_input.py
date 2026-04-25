import customtkinter as ctk
import settings
from view import janela_ctk
from view.janela_ctk import janela, janela_init
from tkinter import messagebox

def atmosfera_input_init(dados_basicos, callback):
    frame_atmosfera = ctk.CTkFrame(janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BG_DARK)
    frame_atmosfera.pack(fill="both", expand=True)

    def make_entry(placeholder, relx, rely):
        entry = ctk.CTkEntry(frame_atmosfera, width=250, height=37, placeholder_text=placeholder,
                             font=(settings.FONT_FAMILY_TECH, 15), fg_color=settings.COLOR_BG_CARD,
                             border_width=1, border_color=settings.COLOR_BORDER,
                             corner_radius=12, text_color=settings.COLOR_TEXT_MAIN)
        entry.place(relx=relx, rely=rely, anchor="center")
        return entry

    label_titulo = ctk.CTkLabel(frame_atmosfera, text="DADOS DA ATMOSFERA:", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 50, "bold"))
    label_titulo.place(relx=0.5, rely=0.1, anchor="center")

    entry_pressao_mar = make_entry("Pressão no Nível do Mar (Pa): ", 0.33, 0.25)
    label_pressao_mar = ctk.CTkLabel(frame_atmosfera, text="Pressão atmosférica ao nível do mar. \n Exemplo: 101325", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_pressao_mar.place(relx=0.33, rely=0.32, anchor="center")

    entry_temperatura_superficie = make_entry("Temperatura na Superfície (K): ", 0.67, 0.25)
    label_temperatura_superficie = ctk.CTkLabel(frame_atmosfera, text="Temperatura na superfície do planeta. \n Exemplo: 288", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_temperatura_superficie.place(relx=0.67, rely=0.32, anchor="center")

    entry_massa_molar = make_entry("Massa Molar do Gás (kg/mol): ", 0.33, 0.45)
    label_massa_molar = ctk.CTkLabel(frame_atmosfera, text="Massa molar do gás principal. \n Exemplo: 0.02897 (ar)", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_massa_molar.place(relx=0.33, rely=0.52, anchor="center")

    entry_gradiente_termico = make_entry("Gradiente Térmico (K/m): ", 0.67, 0.45)
    label_gradiente_termico = ctk.CTkLabel(frame_atmosfera, text="Decaimento de temperatura com altitude. \n Exemplo: -0.0065", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_gradiente_termico.place(relx=0.67, rely=0.52, anchor="center")

    entry_altitude_troposfera = make_entry("Altitude da Troposfera (m): ", 0.33, 0.65)
    label_altitude_troposfera = ctk.CTkLabel(frame_atmosfera, text="Altitude limite da troposfera. \n Exemplo: 11000", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_altitude_troposfera.place(relx=0.33, rely=0.72, anchor="center")

    entry_temperatura_troposfera = make_entry("Temperatura na Troposfera (K): ", 0.67, 0.65)
    label_temperatura_troposfera = ctk.CTkLabel(frame_atmosfera, text="Temperatura na tropopausa. \n Exemplo: 216", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_temperatura_troposfera.place(relx=0.67, rely=0.72, anchor="center")

    def validate_atmosfera(dados_atm):
        errors = []
        for key, value in dados_atm.items():
            if not value.strip():
                errors.append(f"{key}: Campo vazio.")
            else:
                try:
                    num = float(value)
                    if key in ["pressao_mar", "massa_molar", "altitude_troposfera"] and num <= 0:
                        errors.append(f"{key}: Deve ser positivo.")
                except ValueError:
                    errors.append(f"{key}: Deve ser um número válido.")
        if errors:
            messagebox.showerror("Erro de Validação", "\n".join(errors))
            return False
        return True

    def proximo():
        dados_atm = {
            "pressao_mar": entry_pressao_mar.get(),
            "temperatura_superficie": entry_temperatura_superficie.get(),
            "massa_molar": entry_massa_molar.get(),
            "gradiente_termico": entry_gradiente_termico.get(),
            "altitude_troposfera": entry_altitude_troposfera.get(),
            "temperatura_troposfera": entry_temperatura_troposfera.get()
        }
        if validate_atmosfera(dados_atm):
            dados_basicos.update(dados_atm)
            frame_atmosfera.destroy()
            callback(dados_basicos)

    button_proximo = ctk.CTkButton(frame_atmosfera, text="PRÓXIMO", font=(settings.FONT_FAMILY_TECH, 16, "bold"), text_color="white", fg_color=settings.COLOR_ACCENT, hover_color="#14375e", corner_radius=10, height=50, width=400, command=proximo)
    button_proximo.place(relx=0.5, rely=0.9, anchor="center")