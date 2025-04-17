from flask import Flask, render_template, request, jsonify, redirect, session
from calculadora import resolver_expressao
from standup import piada_aleatoria
import json
import random

app = Flask(__name__)
app.secret_key = "supersecreto"

# Carrega memória e conhecimento
with open("data/memoria.json", "r", encoding="utf-8") as f:
    memoria = json.load(f)

with open("data/conhecimento.json", "r", encoding="utf-8") as f:
    conhecimento = json.load(f)

def aprender_novo(fato, valor):
    conhecimento[fato] = valor
    with open("data/conhecimento.json", "w", encoding="utf-8") as f:
        json.dump(conhecimento, f, ensure_ascii=False, indent=4)

def resposta_variada(pergunta):
    respostas = {
        "quem é o seu criador": [
            "Meu criador é Gustavo Ferreira Viana.",
            "Meu criador é o Gustavo, e seu nome completo é Gustavo Ferreira Viana.",
            "O nome do meu criador é Gustavo Ferreira Viana, um prazer conhecê-lo.",
        ]
    }
    return random.choice(respostas.get(pergunta, [])) if pergunta in respostas else None

def aprender_com_texto(texto):
    sentencas = texto.split(".")
    for sentenca in sentencas:
        if sentenca.strip():
            chave = sentenca.strip().lower()
            aprender_novo(chave, sentenca.strip())
    return "Aprendi com o texto que você me enviou!"

@app.route("/")
def video_intro():
    return render_template("video.html")

@app.route("/chat")
def chat():
    if 'messages' not in session:
        session['messages'] = []
    return render_template("chat.html")

@app.route("/mensagens", methods=["GET"])
def mensagens():
    return jsonify(session.get("messages", []))

@app.route("/enviar", methods=["POST"])
def enviar():
    pergunta = request.json["pergunta"].lower().strip()
    session.setdefault("messages", []).append({"from": "user", "text": pergunta})

    if pergunta.startswith("ensinar:"):
        partes = pergunta.replace("ensinar:", "").split("->")
        if len(partes) == 2:
            chave = partes[0].strip()
            resposta = partes[1].strip()
            memoria[chave] = resposta
            with open("data/memoria.json", "w", encoding="utf-8") as f:
                json.dump(memoria, f, ensure_ascii=False, indent=4)
            resposta = "Aprendi com sucesso!"
        else:
            resposta = "Formato inválido. Use: ensinar: pergunta -> resposta"
        session["messages"].append({"from": "bot", "text": resposta})
        session.modified = True
        return jsonify({"resposta": resposta})

    resposta_conta = resolver_expressao(pergunta)
    if "O resultado é" in resposta_conta:
        session["messages"].append({"from": "bot", "text": resposta_conta})
        session.modified = True
        return jsonify({"resposta": resposta_conta})

    if pergunta in ["me conta uma piada", "piada", "me faz rir", "conta uma piada"]:
        piada = piada_aleatoria()
        session["messages"].append({"from": "bot", "text": piada})
        session.modified = True
        return jsonify({"resposta": piada})

    if pergunta.startswith("livro:"):
        texto_livro = pergunta.replace("livro:", "").strip()
        resposta = aprender_com_texto(texto_livro)
        session["messages"].append({"from": "bot", "text": resposta})
        session.modified = True
        return jsonify({"resposta": resposta})

    variada = resposta_variada(pergunta)
    if variada:
        session["messages"].append({"from": "bot", "text": variada})
        session.modified = True
        return jsonify({"resposta": variada})

    if pergunta in memoria:
        resposta = memoria[pergunta]
    elif pergunta in conhecimento:
        resposta = conhecimento[pergunta]
    else:
        resposta = "Ainda não sei responder isso. Me ensine com: ensinar: pergunta -> resposta"

    session["messages"].append({"from": "bot", "text": resposta})
    session.modified = True
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
