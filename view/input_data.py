import customtkinter as ctk
import settings
from view import janela_ctk
from view.janela_ctk import janela, janela_init
from tkinter import messagebox

def input_data_init():
    
    global frame_input_data
    
    frame_input_data = ctk.CTkFrame(janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BG_DARK)
    frame_input_data.pack(fill="both", expand=True)

    def make_entry(placeholder, relx, rely):
        entry = ctk.CTkEntry(frame_input_data, width=250, height=37, placeholder_text=placeholder,
                             font=(settings.FONT_FAMILY_TECH, 15), fg_color=settings.COLOR_BG_CARD,
                             border_width=1, border_color=settings.COLOR_BORDER,
                             corner_radius=12, text_color=settings.COLOR_TEXT_MAIN)
        entry.place(relx=relx, rely=rely, anchor="center")
        return entry

    label_titulo = ctk.CTkLabel(frame_input_data, text="ADICIONE OS DADOS DO SEU FOGUETE:", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 50, "bold"))
    label_titulo.place(relx=0.5, rely=0.1, anchor="center")

    label_coluna_1 = ctk.CTkLabel(frame_input_data, text="Motor & Massa", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 30, "bold"))
    label_coluna_1.place(relx=0.20, rely=0.2, anchor="center")

    entry_empuxo = make_entry("Empuxo do Motor (Newtons): ", 0.20, 0.3)
    
    label_empuxo = ctk.CTkLabel(frame_input_data, text="Força total de saída do motor. \n Exemplo: 10000", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_empuxo.place(relx=0.20, rely=0.35, anchor="center")

    entry_isp = make_entry("ISP do Motor (segundos): ", 0.20, 0.45)

    label_isp = ctk.CTkLabel(frame_input_data, text="Impulso Específico do motor. \n Exemplo: 300", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_isp.place(relx=0.20, rely=0.5, anchor="center")

    entry_massa_seca = make_entry("Massa Seca (kg): ", 0.20, 0.6)

    label_massa_seca = ctk.CTkLabel(frame_input_data, text="Massa do foguete sem combustível. \n Exemplo: 500", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_massa_seca.place(relx=0.20, rely=0.65, anchor="center")

    entry_massa_combustivel = make_entry("Massa do Combustível (kg): ", 0.20, 0.75)

    label_massa_combustivel = ctk.CTkLabel(frame_input_data, text="Massa do combustível. \n Exemplo: 1000", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_massa_combustivel.place(relx=0.20, rely=0.8, anchor="center")

    switch_hohmann = ctk.CTkSwitch(frame_input_data, text="Transferência de Hohmann?", font=(settings.FONT_FAMILY_TECH, 15), text_color=settings.COLOR_TEXT_MAIN, fg_color=settings.COLOR_ACCENT, progress_color="#14375e")
    switch_hohmann.place(relx=0.20, rely=0.85, anchor="center")

    label_hohmann_status = ctk.CTkLabel(frame_input_data, text="Hohmann: Não", text_color="red", font=(settings.FONT_FAMILY_TECH, 15, "bold"))
    label_hohmann_status.place(relx=0.20, rely=0.90, anchor="center")

    def update_hohmann_status():
        if switch_hohmann.get():
            label_hohmann_status.configure(text="Hohmann: Sim", text_color="green")
        else:
            label_hohmann_status.configure(text="Hohmann: Não", text_color="red")

    switch_hohmann.configure(command=update_hohmann_status)

    label_coluna_2 = ctk.CTkLabel(frame_input_data, text="Aerodinâmica & Alvo", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 30, "bold"))
    label_coluna_2.place(relx=0.50, rely=0.2, anchor="center")

    entry_diametro_foguete = make_entry("Diâmetro do Foguete (m): ", 0.50, 0.3)

    label_diametro_foguete = ctk.CTkLabel(frame_input_data, text="Diâmetro do foguete. \n Exemplo: 1.2", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_diametro_foguete.place(relx=0.50, rely=0.35, anchor="center")

    entry_coeficiente_arrasto = make_entry("Coeficiente de Arrasto: ", 0.50, 0.45)

    label_coeficiente_arrasto = ctk.CTkLabel(frame_input_data, text="REFERÊNCIA DE Cd:\n • Ogiva Cônica: 0.50\n • Ogiva Curva: 0.35\n • Von Kármán: 0.25", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_coeficiente_arrasto.place(relx=0.50, rely=0.52, anchor="center")

    entry_altitude_alvo = make_entry("Altitude Alvo (m): ", 0.50, 0.6)

    label_altitude_alvo = ctk.CTkLabel(frame_input_data, text="Altitude alvo para o lançamento. \n Exemplo: 100000", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_altitude_alvo.place(relx=0.50, rely=0.65, anchor="center")
    
    entry_fluxo_massa = make_entry("Fluxo de Massa (kg/s): ", 0.50, 0.75)
    
    label_fluxo_massa = ctk.CTkLabel(frame_input_data, text="Taxa de consumo de combustível. \n Exemplo: 5", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_fluxo_massa.place(relx=0.50, rely=0.8, anchor="center")

    label_coluna_3 = ctk.CTkLabel(frame_input_data, text="Gravidade & Manobra de Giro", text_color=settings.COLOR_ACCENT, font=(settings.FONT_FAMILY_TECH, 30, "bold"))
    label_coluna_3.place(relx=0.80, rely=0.2, anchor="center")

    entry_gravidade = make_entry("Gravidade (m/s²): ", 0.80 , 0.3)

    label_gravidade = ctk.CTkLabel(frame_input_data, text="Aceleração gravitacional local. \n Exemplo: 9.81", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_gravidade.place(relx=0.80, rely=0.35, anchor="center")
    
    entry_raio_planeta = make_entry("Raio do Planeta (Km): ", 0.80, 0.45)

    label_raio_planeta = ctk.CTkLabel(frame_input_data, text="Raio do planeta para cálculo \n de gravidade variável. \n Exemplo: 6371", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_raio_planeta.place(relx=0.80, rely=0.51, anchor="center")

    entry_alt_giro = make_entry("Altitude de Giro (m): ", 0.80, 0.6)

    label_alt_giro = ctk.CTkLabel(frame_input_data, text="Altitude para iniciar a manobra de giro. \n Exemplo: 1000", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_alt_giro.place(relx=0.80, rely=0.65, anchor="center")

    entry_taxa_giro = make_entry("Taxa de Giro (°/km): ", 0.80, 0.75)

    label_taxa_giro = ctk.CTkLabel(frame_input_data, text="Velocidade angular da manobra de giro. \n Exemplo: 0.5", text_color=settings.COLOR_TEXT_SUB, font=(settings.FONT_FAMILY_TECH, 15))
    label_taxa_giro.place(relx=0.80, rely=0.8, anchor="center")

    switch_atmosfera = ctk.CTkSwitch(frame_input_data, text="O planeta tem atmosfera?", font=(settings.FONT_FAMILY_TECH, 15), text_color=settings.COLOR_TEXT_MAIN, fg_color=settings.COLOR_ACCENT, progress_color="#14375e")
    switch_atmosfera.place(relx=0.80, rely=0.85, anchor="center")

    label_atmosfera_status = ctk.CTkLabel(frame_input_data, text="Atmosfera: Não", text_color="red", font=(settings.FONT_FAMILY_TECH, 15, "bold"))
    label_atmosfera_status.place(relx=0.80, rely=0.90, anchor="center")

    def update_atmosfera_status():
        if switch_atmosfera.get():
            label_atmosfera_status.configure(text="Atmosfera: Sim", text_color="green")
        else:
            label_atmosfera_status.configure(text="Atmosfera: Não", text_color="red")

    switch_atmosfera.configure(command=update_atmosfera_status)

    def validate_data(dados):
        errors = []
        for key, value in dados.items():
            if isinstance(value, str):
                if not value.strip():
                    errors.append(f"{key}: Campo vazio.")
                else:
                    try:
                        num = float(value)
                        if num <= 0:
                            errors.append(f"{key}: Deve ser um número positivo.")
                    except ValueError:
                        errors.append(f"{key}: Deve ser um número válido.")
        if errors:
            messagebox.showerror("Erro de Validação", "\n".join(errors))
            return False
        return True

    def simular():
        dados = {
            "empuxo": entry_empuxo.get(),
            "isp": entry_isp.get(),
            "massa_seca": entry_massa_seca.get(),
            "massa_combustivel": entry_massa_combustivel.get(),
            "diametro_foguete": entry_diametro_foguete.get(),
            "coeficiente_arrasto": entry_coeficiente_arrasto.get(),
            "altitude_alvo": entry_altitude_alvo.get(),
            "fluxo_massa": entry_fluxo_massa.get(),
            "gravidade": entry_gravidade.get(),
            "raio_planeta": entry_raio_planeta.get(),
            "alt_giro": entry_alt_giro.get(),
            "taxa_giro": entry_taxa_giro.get(),
            "tem_atmosfera": switch_atmosfera.get(),
            "transferencia_hohmann": switch_hohmann.get()
        }
        if validate_data(dados):
            frame_input_data.destroy()
            def next_step(current_dados):
                if current_dados.get("tem_atmosfera") and "pressao_mar" not in current_dados:
                    from view.atmosfera_input import atmosfera_input_init
                    atmosfera_input_init(current_dados, next_step)
                elif current_dados.get("transferencia_hohmann") and "orbita_inicial" not in current_dados:
                    from view.hohmann_input import hohmann_input_init
                    hohmann_input_init(current_dados, next_step)
                else:
                    from core.simulation_engine import calculate
                    calculate(current_dados)
            next_step(dados)

    button_simular = ctk.CTkButton(frame_input_data, text="SIMULAR", font=(settings.FONT_FAMILY_TECH, 16, "bold"), text_color="white", fg_color=settings.COLOR_ACCENT, hover_color="#14375e", corner_radius=10, height=50, width=400, command=simular)
    button_simular.place(relx=0.5, rely=0.93, anchor="center")