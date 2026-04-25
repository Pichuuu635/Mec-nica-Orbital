import math

def calculate(dados):
    try:
        empuxo = float(dados["empuxo"])
        isp = float(dados["isp"])
        m_seca = float(dados["massa_seca"])
        m_fuel = float(dados["massa_combustivel"])
        raio_p = float(dados["raio_planeta"]) * 1000  # Km para metros
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
            temperatura_troposfera = float(dados["temperatura_troposfe      ra"])
            
        else:
            print("Sem dados da atmosfera.")

        transferencia_hohmann = dados.get("transferencia_hohmann", False)
        if transferencia_hohmann and "orbita_inicial" in dados:
            orbita_inicial = float(dados["orbita_inicial"])
            orbita_final = float(dados["orbita_final"])
            velocidade_inicial = float(dados["velocidade_inicial"])
            velocidade_final = float(dados["velocidade_final"])
            delta_v1 = float(dados["delta_v1"])
            delta_v2 = float(dados["delta_v2"])
            
        else:
            print("Sem dados da transferência de Hohmann.")

        # Variaveis para simulação
        tempo = 0
        dt = 0.1
        altitude_total = raio_p + altitude_alvo
        massa_total = m_seca + m_fuel
        velocidade = 0
        altitude = 0
        angulo = 90
        g_no_alvo = gravidade_variavel(g_local, raio_p, altitude_alvo)
        v_orbital = velocidade_orbital(g_no_alvo, altitude_total)
        area_f = area_frontal(diametro_foguete)
        constante_gases = 8.314
        pressao_trop = pressao_mar * (1 + ((gradiente_termico + altitude_troposfera)/temperatura_superficie))**((-g_local*massa_molar)/constante_gases*gradiente_termico)
        
        print(f"Velocidade orbital no alvo: {v_orbital} m/s")


    
        while massa_total > m_seca:
            
            temp_local = calcular_temperatura_local(temperatura_superficie, gradiente_termico,
                                       altitude, altitude_troposfera, temperatura_troposfera)
            pressao_local = calcular_pressao_local(pressao_mar, gradiente_termico, altitude, 
                                   temperatura_superficie, g_local, massa_molar, constante_gases,
                                     altitude_troposfera, temperatura_troposfera, pressao_trop)
            
            calcular_rho(pressao_local, massa_molar, constante_gases, temp_local)
            
            
            



    except Exception as e:
        print(f"Erro no processamento físico: {e}")

#Funções de Cálculo de parâmetros orbitais, manobras, etc...

def gravidade_variavel(g_local, raio_p, altitude):
    g_var = g_local * (raio_p / (raio_p + altitude))**2
    return g_var

def velocidade_orbital(g_var, altitude_total):
    velocidade_orbital = math.sqrt(g_var * altitude_total)
    return velocidade_orbital

def area_frontal(diametro):
    a_frontal = math.pi * (diametro/2)**2
    return a_frontal

def calcular_temperatura_local(temp_sup, grad_term, alt, alt_trop, temp_trop):
    if alt < alt_trop:
        temp_local = temp_sup + (grad_term * alt)
    else:
        temp_local = temp_trop
    return temp_local

def calcular_pressao_local(p_mar, grad_term, alt, temp_sup, g, m_molar, const_gases, alt_trop, temp_trop, pressao_tropos):
    if alt < alt_trop:
        pressao_local = p_mar * (1 + ((grad_term * alt)/temp_sup))**((-g*m_molar)/const_gases*grad_term)
    else:
        alt_subida = alt - alt_trop
        pressao_local = pressao_tropos * math.e**((-g*m_molar*alt_subida)/const_gases*temp_trop)
        return pressao_local

def calcular_rho(p_local, m_molar, const_gas, temp_local):

    rho = (p_local * m_molar)/(const_gas * temp_local)

    return rho

