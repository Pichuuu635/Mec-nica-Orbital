WIDTH = 1920
HEIGHT = 1080
GEOMETRY = f"{WIDTH}x{HEIGHT}"

#COLORS

COLOR_BG_DARK = "#0B0D17"        # Fundo principal da janela (Espaço Profundo)
COLOR_BG_CARD = "#161B22"        # Fundo de frames e áreas de inputs
COLOR_BORDER  = "#30363D"        # Bordas de botões e divisores técnicos

COLOR_TEXT_MAIN = "#FFFFFF"      # Texto principal (Leitura de dados e títulos)
COLOR_TEXT_SUB  = "#8B949E"      # Texto secundário (Unidades: km/s, kg, m/s²)
COLOR_ACCENT    = "#00D1FF"      # Cor de destaque (Labels importantes e botões)

COLOR_THRUST    = "#F0883E"      # Cor para empuxo/motores (Laranja fogo)
COLOR_ORBIT     = "#7D52FF"      # Cor para trajetória orbital bem-sucedida
COLOR_DRAG      = "#58A6FF"      # Cor para representar arrasto/atmosfera

COLOR_SUCCESS   = "#00FF41"      # Status nominal: "Órbita Alcançada"
COLOR_WARNING   = "#FFD700"      # Alerta: "Max-Q" (Pressão máxima estrutural)
COLOR_DANGER    = "#FF4B4B"      # Erro crítico: "Falha de Ignição" ou "Reentrada"

# Fontes para a Interface (Menus, Botões, Instruções)
FONT_FAMILY_MAIN = "Segoe UI"      # Padrão moderno e limpo (Windows)
FONT_FAMILY_ALT  = "Helvetica"     # Alternativa elegante para Mac/Linux

# Fontes para Telemetria (Dados Numéricos, Logs, Terminal)
FONT_FAMILY_TECH = "Consolas"      # Visual de código da NASA (Windows)
FONT_FAMILY_MONO = "Roboto Mono"   # Alternativa futurista (precisa estar instalada)

#Aqui estão as opções mais comuns que você pode usar:
#"bold": Deixa a fonte negrito. Ideal para títulos e botões de ação (como o "IGNITION").
#"italic": Deixa a fonte itálico. Ótimo para notas de rodapé ou legendas de unidades (ex: m/s²).
#"underline": Adiciona um sublinhado. Útil para links ou destaques críticos.
#"overstrike": Cria um efeito de riscado (menos comum em UIs aeroespaciais).
#"normal": É o padrão. Se você não colocar nada, o sistema assume esta.
