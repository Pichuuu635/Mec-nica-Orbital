import math
import matplotlib.pyplot as plt

def calculate(dados):
    try:
        # --- CARREGAMENTO DE DADOS ---
        empuxo = float(dados["empuxo"])
        isp = float(dados["isp"])
        m_seca = float(dados["massa_seca"])
        m_fuel = float(dados["massa_combustivel"])
        raio_p = float(dados["raio_planeta"]) * 1000  
        g_local = float(dados["gravidade"])
        fluxo_massa = float(dados["fluxo_massa"])
        diametro_foguete = float(dados["diametro_foguete"])
        coef_arrasto = float(dados["coeficiente_arrasto"])
        altitude_alvo = float(dados["altitude_alvo"])
        alt_giro = float(dados["alt_giro"])
        taxa_giro = float(dados["taxa_giro"])

        tem_atmosfera = dados.get("tem_atmosfera", False)
        if tem_atmosfera and "pressao_mar" in dados:
            pressao_mar = float(dados["pressao_mar"])
            temperatura_superficie = float(dados["temperatura_superficie"])
            massa_molar = float(dados["massa_molar"])
            gradiente_termico = float(dados["gradiente_termico"])
            altitude_troposfera = float(dados["altitude_troposfera"])
            temperatura_troposfera = float(dados["temperatura_troposfera"])
            atmosfera = True
        else:
            atmosfera = False

        # --- VARIÁVEIS DE ESTADO ---
        tempo, dt = 0, 0.1
        massa_total = m_seca + m_fuel
        vx, vy, altitude, angulo = 0.0, 0.0, 0.0, 90.0
        area_f = area_frontal(diametro_foguete)
        constante_gases = 8.314
        ultimo_rho = 999.0
        rho, f_arrasto = 0.0, 0.0
        
        lista_alt, lista_vel, lista_tempo = [], [], []

        if atmosfera:
            pressao_trop = pressao_mar * (1 + ((gradiente_termico * altitude_troposfera)/temperatura_superficie))**((-g_local*massa_molar)/(constante_gases*gradiente_termico))
        
        print(f"Iniciando Simulação de Lançamento...")

        while massa_total > m_seca:
            # --- 1. LÓGICA DO MOTOR E CORTE (MECO) ---
            if altitude >= altitude_alvo or massa_total <= m_seca:
                # MOMENTO DO DESLIGAMENTO: CALCULA A ÓRBITA AQUI!
                v_final = math.sqrt(vx**2 + vy**2)
                mu = g_local * (raio_p**2)
                r_final = raio_p + altitude
                
                # Energia e Momento Angular
                energia = (v_final**2 / 2) - (mu / r_final)
                h_angular = r_final * v_final * math.cos(math.radians(angulo))
                
                print("-" * 30)
                print(f" MOTOR DESLIGADO (MECO) aos {tempo:.1f}s")
                
                if energia >= 0:
                    print(" TRAJETÓRIA DE ESCAPE! (O foguete não volta)")
                else:
                    valor_exc = 1 + (2 * energia * h_angular**2) / mu**2
                    excentricidade = math.sqrt(max(0, valor_exc))
                    semieixo = -mu / (2 * energia)
                    periastro = (semieixo * (1 - excentricidade) - raio_p) / 1000
                    apoastro = (semieixo * (1 + excentricidade) - raio_p) / 1000
                    
                    print(f" Periastro: {periastro:.2f} km")
                    print(f" Apoastro: {apoastro:.2f} km")
                    if periastro > 100:
                        print(" ÓRBITA ESTÁVEL ATINGIDA! 🛰️")
                    else:
                        print(" ÓRBITA INSTÁVEL (Reentrada Garantida)")
                print("-" * 30)
                break # Encerra a simulação no corte do motor

            # --- 2. GIRO DE GRAVIDADE ---
            if altitude > alt_giro:
                angulo -= taxa_giro * dt
            if angulo < 0: angulo = 0
            rad = math.radians(angulo)

            # --- 3. AMBIENTE (RHO) ---
            if atmosfera:
                temp_local = calcular_temperatura_local(temperatura_superficie, gradiente_termico, altitude, altitude_troposfera, temperatura_troposfera)
                pressao_local = calcular_pressao_local(pressao_mar, gradiente_termico, altitude, temperatura_superficie, g_local, massa_molar, constante_gases, altitude_troposfera, temperatura_troposfera, pressao_trop)
                rho = calcular_rho(pressao_local, massa_molar, constante_gases, temp_local) if pressao_local > 0.5 else 0.0
                if rho > ultimo_rho: rho = ultimo_rho # Trava para evitar saltos
                ultimo_rho = rho
            else:
                rho = 0.0

            # --- 4. FÍSICA DO MOVIMENTO ---
            v_total = math.sqrt(vx**2 + vy**2)
            f_arrasto = calcular_arrasto(rho, v_total, coef_arrasto, area_f)
            g_atual = gravidade_variavel(g_local, raio_p, altitude)

            forca_y = (empuxo * math.sin(rad)) - (f_arrasto * math.sin(rad)) - (massa_total * g_atual)
            forca_x = (empuxo * math.cos(rad)) - (f_arrasto * math.cos(rad))

            ax, ay = forca_x / massa_total, forca_y / massa_total
            vx += ax * dt
            vy += ay * dt
            altitude += vy * dt
            
            massa_total -= fluxo_massa * dt
            tempo += dt

            # Listas para o gráfico
            lista_alt.append(altitude)
            lista_vel.append(v_total)
            lista_tempo.append(tempo)

            if int(tempo / dt) % int(1/dt) == 0:
                print(f"T: {tempo:.0f}s | Alt: {altitude/1000:.1f}km | Vel: {v_total:.1f}m/s | Ang: {angulo:.1f}°")

        # --- GRÁFICO FINAL ---
         # --- CÁLCULOS PÓS-VOO (ÓRBITA) ---
        v_final = v_total
        r_final = raio_p + altitude
        mu = g_local * (raio_p**2)
        
        # Energia orbital específica
        energia = (v_final**2 / 2) - (mu / r_final)
        # Momento angular (Horizontalidade)
        h_angular = r_final * v_final * math.cos(math.radians(angulo))
        
        print("\n" + "="*40)
        print(f"       RELATÓRIO FINAL DE MISSÃO")
        print("="*40)

        if energia >= 0:
            print(f" ESTADO: ESCAPE INTERPLANETÁRIO 🌌")
            print(f" VELOCIDADE FINAL: {v_final:.2f} m/s")
            print(f" ALTITUDE FINAL: {altitude/1000:.2f} km")
            print(f" Nota: O foguete superou a gravidade da Terra.")
        else:
            try:
                valor_exc = 1 + (2 * energia * h_angular**2) / mu**2
                excentricidade = math.sqrt(max(0, valor_exc))
                semieixo = -mu / (2 * energia)
                
                peri = (semieixo * (1 - excentricidade) - raio_p) / 1000
                apo = (semieixo * (1 + excentricidade) - raio_p) / 1000
                
                print(f" Periastro: {peri:.2f} km")
                print(f" Apoastro: {apo:.2f} km")
                
                if peri > 100:
                    print(" STATUS: ÓRBITA ESTÁVEL ATINGIDA! 🛰️")
                else:
                    print(" STATUS: ÓRBITA INSTÁVEL (Vai queimar na atmosfera)")
            except:
                print(" Erro ao calcular elipse (Trajetória extrema)")

        print("="*40)

        # O PLOT PRECISA ESTAR AQUI FORA DO TRY INTERNO
        plt.figure(figsize=(10, 5))
        plt.plot(lista_tempo, [a/1000 for a in lista_alt], label="Altitude (km)", color="blue")
        plt.title("Trajetória de Voo")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Altitude (km)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Erro no processamento físico: {e}")

# --- FUNÇÕES DE APOIO ---
def gravidade_variavel(g_local, raio_p, altitude):
    return g_local * (raio_p / (raio_p + altitude))**2

def area_frontal(diametro):
    return math.pi * (diametro/2)**2

def calcular_temperatura_local(temp_sup, grad_term, alt, alt_trop, temp_trop):
    return temp_sup + (grad_term * alt) if alt < alt_trop else temp_trop

def calcular_pressao_local(p_mar, grad_term, alt, temp_sup, g, m_molar, const_gases, alt_trop, temp_trop, pressao_tropos):
    if alt < alt_trop:
        return p_mar * (1 + ((grad_term * alt)/temp_sup))**((-g*m_molar)/(const_gases*grad_term))
    return pressao_tropos * math.e**((-g*m_molar*(alt-alt_trop))/(const_gases*temp_trop))

def calcular_rho(p_local, m_molar, const_gas, temp_local):
    if temp_local <= 0: return 0.0
    return (p_local * m_molar)/(const_gas * temp_local)

def calcular_arrasto(rho, velocidade, cd, area):
    return 0.5 * rho * (velocidade**2) * cd * area
