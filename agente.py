# Titulo

# Campo de Mensagem

# Quando o Usuario enviar uma mensagem:
    # Mostrar a mensagem na conversa;
    # Mandar a mensagem para IA;
    # Mostrar a resposta da IA pro Usuario.

# Ferramentas:
    # streamlit e openai

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI( api_key="CHAVE_API_GEMINI", base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

st.write("## ChatBot com IA") # Hashtag(#) serve para o texto ficar maior

# Historico de Mensagens:
if not "lista_mensagens" in st.session_state: # .session_state -> memoria do streamlit

    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input(
    "Escreva sua mensagem aqui"
) # chat_input -> campo de mensagem

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]

    st.chat_message(quem_enviou).write(texto_mensagem)

if mensagem_usuario:

    # Se enviou texto

    st.chat_message("user").write(mensagem_usuario) # chat_message -> exibe a mensagem do usuario na tela

    # user -> usuario

    mensagem1 = {
        "role": "user",
        "content": mensagem_usuario
    }

    st.session_state["lista_mensagens"].append(mensagem1)

    # Respostas Inteligentes:
    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["lista_mensagens"],  model="gemini-flash-lite-latest") # .chat.completions.create -> CHAT -> conversa da IA | COMPLETATIONS -> resposta da IA  com base no seu texto! | CREATE() -> resposta conpleta da IA

    resposta_ia = resposta_ia.choices[0].message.content 
    # .choices -> acessa as opções de resposta geradas pela IA
    # [0]      -> pega a primeira opção de resposta
    # .message -> acessa a mensagem dessa resposta
    # .content -> pega somente o texto da mensagem

    st.chat_message("assistant").write(resposta_ia) # chat_message -> exibe a mensagem da IA na tela
    # assistant -> IA/robo

    mensagem2 = {
        "role": "assistant",
        "content": resposta_ia
    }

    st.session_state["lista_mensagens"].append(mensagem2)