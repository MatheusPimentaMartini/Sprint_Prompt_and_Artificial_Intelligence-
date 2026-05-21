import gradio as gr
import re


# -------------------------
# API simulada
# -------------------------

carregadores = {
    "GW-01": {
        "status": "Disponível",
        "potencia_atual": "0 kW",
        "energia_consumida": "0 kWh",
        "horario_sessao": "-",
        "usuario_conectado": "-"
    },

    "GW-02": {
        "status": "Em uso",
        "potencia_atual": "22 kW",
        "energia_consumida": "45 kWh",
        "horario_sessao": "18:35",
        "usuario_conectado": "Carlos Silva"
    },

    "GW-03": {
        "status": "Offline",
        "potencia_atual": "-",
        "energia_consumida": "-",
        "horario_sessao": "-",
        "usuario_conectado": "-"
    }
}


ultimo_carregador_consultado = None


# -------------------------
# Extrair carregador
# -------------------------

def extrair_carregador(pergunta):

    pergunta = pergunta.upper()

    resultado = re.search(r"GW-\d+", pergunta)

    if resultado:
        return resultado.group()

    numero = re.search(r"\d+", pergunta)

    if numero:
        return f"GW-{numero.group().zfill(2)}"

    return None


# -------------------------
# Identificar intenção
# -------------------------

def identificar_intencao(pergunta):

    pergunta = pergunta.lower()

    if "quem" in pergunta or "usuário" in pergunta or "usuario" in pergunta:
        return "usuario"

    elif "potência" in pergunta or "potencia" in pergunta or "kw" in pergunta:
        return "potencia"

    elif "energia" in pergunta or "consumiu" in pergunta or "kwh" in pergunta:
        return "energia"

    elif "horário" in pergunta or "horario" in pergunta:
        return "horario"

    elif "status" in pergunta or "situação" in pergunta or "situacao" in pergunta:
        return "status"

    return "resumo"


# -------------------------
# Resumo operacional
# -------------------------

def gerar_resumo(id_carregador, dados):

    status = dados["status"]

    if status == "Disponível":
        return f"O carregador {id_carregador} está disponível para nova recarga."

    elif status == "Em uso":
        return f"O carregador {id_carregador} está operando em {dados['potencia_atual']} para {dados['usuario_conectado']}."

    elif status == "Offline":
        return f"O carregador {id_carregador} está offline."

    return "Status desconhecido."


# -------------------------
# Chatbot
# -------------------------

def chatbot(pergunta, history):

    global ultimo_carregador_consultado

    id_encontrado = extrair_carregador(pergunta)

    if id_encontrado:
        ultimo_carregador_consultado = id_encontrado
    else:
        id_encontrado = ultimo_carregador_consultado


    if not id_encontrado or id_encontrado not in carregadores:

        return "Não encontrei o carregador."


    dados = carregadores[id_encontrado]

    intencao = identificar_intencao(pergunta)


    if intencao == "usuario":
        return f"O carregador {id_encontrado} está sendo usado por {dados['usuario_conectado']}."

    elif intencao == "potencia":
        return f"A potência atual é {dados['potencia_atual']}."

    elif intencao == "energia":
        return f"O consumo atual é {dados['energia_consumida']}."

    elif intencao == "horario":
        return f"A sessão começou às {dados['horario_sessao']}."

    elif intencao == "status":
        return f"O status atual é {dados['status']}."


    resumo = gerar_resumo(id_encontrado, dados)

    return f"""
Carregador: {id_encontrado}

Status: {dados["status"]}

Potência atual: {dados["potencia_atual"]}

Energia consumida: {dados["energia_consumida"]}

Horário: {dados["horario_sessao"]}

Usuário: {dados["usuario_conectado"]}

Resumo:
{resumo}
"""


# -------------------------
# Interface
# -------------------------

interface = gr.ChatInterface(
    fn=chatbot,

    title="⚡ GoodWe ChargeOps Assistant",

    description="""
Assistente inteligente para operadores comerciais.

Capacidades:
✅ Consultar status
✅ Verificar potência
✅ Consultar usuário conectado
✅ Monitoramento operacional
""",

    textbox=gr.Textbox(
        placeholder="Digite sua pergunta...",
        label="Pergunta do Operador"
    ),

    examples=[
        "Qual o status do GW-02?",
        "Quem está usando o GW-02?",
        "Qual a potência do carregador 2?",
        "Quanto ele consumiu?",
        "Status do carregador 3"
    ]
)

interface.launch()