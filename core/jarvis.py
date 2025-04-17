import json
import os

class JARVIS:
    def __init__(self):
        self.memoria_path = "data/memoria.json"
        self.conhecimento = self.carregar_memoria()

    def carregar_memoria(self):
        if os.path.exists(self.memoria_path):
            with open(self.memoria_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def salvar_memoria(self):
        with open(self.memoria_path, "w", encoding="utf-8") as f:
            json.dump(self.conhecimento, f, indent=4, ensure_ascii=False)

    def ensinar(self, pergunta, resposta):
        self.conhecimento[pergunta.lower()] = resposta
        self.salvar_memoria()

    def responder(self, pergunta):
        pergunta = pergunta.lower()
        return self.conhecimento.get(pergunta, "Ainda não aprendi isso. Me ensine!")

