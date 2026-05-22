# Sprint_Prompt_and_Artificial_Intelligence

# GoodWe ChargeOps Assistant

## Descrição do Projeto

O GoodWe ChargeOps Assistant é um chatbot inteligente desenvolvido para o GoodWe EV Challenge 2026.

O sistema foi projetado para auxiliar operadores comerciais no monitoramento de carregadores elétricos através de linguagem natural, utilizando regras de interpretação, extração de informações com Regex, memória simples de contexto e uma base simulada de carregadores.

O chatbot atua como uma interface inteligente entre operadores e o sistema de gerenciamento energético, permitindo tomadas de decisão mais rápidas e eficientes.

---

# Problema

Em eletropostos comerciais com múltiplos veículos conectados simultaneamente, a ausência de gerenciamento inteligente dificulta o controle da distribuição de potência, aumenta riscos de sobrecarga elétrica e reduz a eficiência energética da operação.

Além disso, operadores possuem dificuldade em monitorar consumo, utilização dos carregadores e tomada de decisões em tempo real.

---

# Objetivo

Criar um chatbot inteligente para operadores comerciais capaz de:

- Consultar status dos carregadores
- Monitorar consumo energético
- Identificar possíveis sobrecargas
- Auxiliar decisões operacionais
- Interpretar informações em linguagem natural
- Sugerir ações preventivas para otimização energética

---

# Sustentabilidade

Nossa solução está alinhada aos objetivos do EV Challenge GoodWe:

- Redução do desperdício energético através de monitoramento inteligente
- Apoio ao gerenciamento eficiente da potência distribuída
- Possibilidade de integração futura com energia solar
- Menor risco de sobrecarga elétrica
- Maior eficiência operacional

### Impactos esperados

### Ambiental

- Redução do desperdício energético
- Uso mais eficiente dos recursos energéticos

### Tecnológico

- Maior automação operacional
- Melhor monitoramento em tempo real

### Econômico

- Redução de custos operacionais
- Maior eficiência no gerenciamento dos carregadores

---

# Persona

## Operador Comercial

Responsável por:

- Monitorar carregadores
- Acompanhar utilização
- Apoiar decisões operacionais
- Gerenciar recursos energéticos

---

# Tecnologias Utilizadas

- Python
- Gradio
- Regex (re)
- Estruturas condicionais
- Memória simples de contexto
- API simulada de carregadores
- Ambiente Virtual (.venv)

---

# Como executar o projeto

## Pré-requisitos

Antes de iniciar, instale:

- Python 3.10 ou superior
- Git

Verificar versões:

```bash
python --version
```

```bash
git --version
```

---

## 1 Clonar repositório

```bash
git clone https://github.com/seu-usuario/Sprint_Prompt_and_Artificial_Intelligence.git
```

Entrar na pasta:

```bash
cd Sprint_Prompt_and_Artificial_Intelligence
```

---

## 2 Criar ambiente virtual

Criar ambiente:

```bash
python -m venv .venv
```

---

## 3 Ativar ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

Após ativar aparecerá algo parecido com:

```bash
(.venv)
```

---

## 4 Instalar dependências

Instalar bibliotecas:

```bash
pip install -r requirements.txt
```

Caso ainda não exista arquivo requirements:

```bash
pip install gradio
```

---

## 5 Executar chatbot

Executar:

```bash
python app.py
```

ou:

```bash
python main.py
```

---

## 6 Acessar interface

Após executar, o terminal mostrará algo parecido:

```bash
Running on local URL:

http://127.0.0.1:7860
```

Abra no navegador:

```text
http://127.0.0.1:7860
```

---

# Arquitetura do Sistema

```text
Operador Comercial
        ↓
Interface Gradio
        ↓
Recebimento da pergunta
        ↓
Validação da entrada
        ↓
Extração do carregador (Regex)
        ↓
Identificação da intenção
        ↓
Consulta de dados do carregador
        ↓
Processamento da informação
        ↓
Geração de resposta inteligente
        ↓
Resposta ao operador
```

---

# Funcionalidades

✅ Consultar status dos carregadores

✅ Verificar potência atual

✅ Consultar consumo energético

✅ Informar riscos de sobrecarga

✅ Informar fonte de energia utilizada

✅ Gerar recomendações operacionais

✅ Interpretar perguntas em linguagem natural

✅ Manter contexto da conversa

---

# Dados utilizados via API simulada

- id_carregador
- status
- potencia_atual
- limite_potencia
- energia_consumida
- horario_sessao
- usuario_conectado
- fonte_energia
- risco_sobrecarga

---

# Modelo de Teste

### Pergunta

```text
Qual o status do GW-02?
```

Resposta esperada:

```text
Status atual: Em uso.
```

### Pergunta

```text
Quem está usando o GW-02?
```

Resposta esperada:

```text
Carlos Silva.
```

### Pergunta

```text
Quanto o GW-02 consumiu?
```

Resposta esperada:

```text
45 kWh.
```

### Pergunta

```text
Existe risco de sobrecarga no GW-02?
```

Resposta esperada:

```text
Risco de sobrecarga: Médio.
```

### Pergunta

```text
Qual a fonte de energia do GW-01?
```

Resposta esperada:

```text
Fonte atual: Solar.
```

---

# Estrutura do Projeto

```text
Sprint_Prompt_and_Artificial_Intelligence/

│── app.py
│── requirements.txt
│── README.md
│── .venv
```

---

# System Prompt

Você é o GoodWe ChargeOps Assistant.

Contexto:

Você trabalha em um sistema inteligente de recarga de veículos elétricos da GoodWe para ambientes comerciais.

Persona atendida:

Operador Comercial.

Você deve:

- informar status dos carregadores;
- mostrar potência atual;
- informar consumo energético;
- identificar riscos de sobrecarga;
- informar fonte de energia utilizada;
- auxiliar monitoramento operacional;
- sugerir recomendações preventivas;
- responder utilizando linguagem técnica e objetiva.

Você NÃO deve:

- responder assuntos fora do sistema;
- inventar informações;
- gerar diagnósticos sem dados disponíveis;
- alterar dados operacionais.

---

# Diferenciais da Solução

- Utilização de linguagem natural

- Monitoramento inteligente dos carregadores

- Identificação de riscos de sobrecarga

- Integração simulada com energia solar

- Sistema preparado para expansão com IA

- Memória simples para continuidade da conversa

---

# Conclusão

O GoodWe ChargeOps Assistant foi desenvolvido como uma interface inteligente entre operadores comerciais e sistemas de recarga elétrica.

A solução busca melhorar o monitoramento operacional, reduzir desperdícios energéticos e apoiar decisões relacionadas ao gerenciamento inteligente de potência, alinhando-se aos objetivos do GoodWe EV Challenge 2026.

---

# Integrantes

Leonardo Soares Rodrigues — RM: 572986 

Matheus Pimenta — RM: 569400

Rubens Henrique — RM: 572667

Guilherme Cedro — RM: 571050

Gabriel Carvalho — RM: 571381

Eduardo — RM: 572514