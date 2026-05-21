import gradio as gr
import re


# -------------------------
# API simulada
# -------------------------

carregadores = {
    "GW-01": {
        "status": "Disponível",
        "potencia_atual": 0,
        "limite_potencia": 22,
        "energia_consumida": 0,
        "horario_sessao": "-",
        "usuario_conectado": "-",
        "fonte_energia": "Solar",
        "risco_sobrecarga": "Baixo"
    },

    "GW-02": {
        "status": "Em uso",
        "potencia_atual": 22,
        "limite_potencia": 22,
        "energia_consumida": 45,
        "horario_sessao": "18:35",
        "usuario_conectado": "Carlos Silva",
        "fonte_energia": "Solar + Rede",
        "risco_sobrecarga": "Médio"
    },

    "GW-03": {
        "status": "Offline",
        "potencia_atual": 0,
        "limite_potencia": 22,
        "energia_consumida": 0,
        "horario_sessao": "-",
        "usuario_conectado": "-",
        "fonte_energia": "-",
        "risco_sobrecarga": "Indisponível"
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

    elif "sobrecarga" in pergunta or "risco" in pergunta or "pico" in pergunta:
        return "sobrecarga"

    elif "fonte" in pergunta or "solar" in pergunta or "renovável" in pergunta:
        return "fonte"

    elif "recomendação" in pergunta or "recomenda" in pergunta or "melhor horário" in pergunta:
        return "recomendacao"

    elif "status" in pergunta or "situação" in pergunta or "situacao" in pergunta:
        return "status"

    return "resumo"


# -------------------------
# Resumo operacional
# -------------------------

def gerar_resumo(id_carregador, dados):

    status = dados["status"]

    if status == "Disponível":
        return f"O carregador {id_carregador} está disponível para nova recarga. Recomenda-se priorizar seu uso para balancear a demanda."

    elif status == "Em uso":
        return f"O carregador {id_carregador} está operando em {dados['potencia_atual']} kW para {dados['usuario_conectado']}. Risco de sobrecarga: {dados['risco_sobrecarga']}."

    elif status == "Offline":
        return f"O carregador {id_carregador} está offline. Recomenda-se acionar a equipe técnica para verificar comunicação, energia ou manutenção."

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
        return "Não encontrei o carregador. Informe um código como GW-01, GW-02 ou GW-03."

    dados = carregadores[id_encontrado]

    intencao = identificar_intencao(pergunta)

    if intencao == "usuario":
        return f"O carregador {id_encontrado} está sendo usado por {dados['usuario_conectado']}."

    elif intencao == "potencia":
        return f"A potência atual é {dados['potencia_atual']} kW."

    elif intencao == "energia":
        return f"O consumo atual é {dados['energia_consumida']} kWh."

    elif intencao == "horario":
        return f"A sessão começou às {dados['horario_sessao']}."

    elif intencao == "status":
        return f"O status atual é {dados['status']}."

    elif intencao == "sobrecarga":
        return f"""
Risco de sobrecarga: {dados['risco_sobrecarga']}

Análise:
A potência atual é de {dados['potencia_atual']} kW, com limite operacional de {dados['limite_potencia']} kW.

Recomendação:
Caso o risco aumente, o sistema deve reduzir a potência ou redistribuir a carga entre carregadores disponíveis.
"""

    elif intencao == "fonte":
        return f"""
Fonte de energia atual: {dados['fonte_energia']}

Análise:
O uso de energia solar contribui para reduzir o consumo da rede elétrica e melhora a sustentabilidade da operação.
"""

    elif intencao == "recomendacao":
        return f"""
Recomendação operacional:

Priorizar carregadores disponíveis, evitar horários de pico e monitorar carregadores operando no limite de potência.

Para este carregador:
Status: {dados['status']}
Potência atual: {dados['potencia_atual']} kW
Risco de sobrecarga: {dados['risco_sobrecarga']}
"""

    resumo = gerar_resumo(id_encontrado, dados)

    return f"""
Carregador: {id_encontrado}

Status: {dados["status"]}

Potência atual: {dados["potencia_atual"]} kW

Limite de potência: {dados["limite_potencia"]} kW

Energia consumida: {dados["energia_consumida"]} kWh

Horário: {dados["horario_sessao"]}

Usuário: {dados["usuario_conectado"]}

Fonte de energia: {dados["fonte_energia"]}

Risco de sobrecarga: {dados["risco_sobrecarga"]}

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
Assistente inteligente para operadores comerciais de eletropostos GoodWe.

Capacidades:
✅ Consultar status dos carregadores
✅ Verificar potência atual
✅ Consultar consumo energético
✅ Identificar risco de sobrecarga
✅ Informar fonte de energia
✅ Gerar recomendações operacionais
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
        "Existe risco de sobrecarga no GW-02?",
        "Qual a fonte de energia do GW-01?",
        "Qual a recomendação operacional para o GW-02?"
    ]
)

interface.launch()