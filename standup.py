import random

piadas = [
    "Por que o Java foi ao terapeuta? Porque ele tinha problemas de classe.",
    "Qual o cúmulo da paciência? Esperar um programa em Python rodar sem usar o asyncio.",
    "Por que o programador morreu no chuveiro? Porque ele leu o shampoo: 'Enxágue e repita'.",
    "O que o zero disse para o oito? Belo cinto!",
    "Qual o animal mais antigo do mundo? A zebra, porque é preta e branca.",
    "Você sabe qual é o café mais perigoso do mundo? O café assassinato.",
    "Por que o gato entrou na igreja? Porque ele queria virar um católico.",
    "Como o elétron atende ao telefone? Próton!",
    "Por que o notebook foi preso? Porque ele executou um programa ilegal.",
    "Como o Batman faz para entrar na Batcaverna? Com o Bat-chave.",
    "O que o tomate disse para o outro? Não se preocupe, ketchup!",
    "Por que o jacaré tirou o filho da escola? Porque ele réptil de ano.",
    "Como se chama um boi dormindo? Boi-cote.",
    "Por que a vaca foi para o espaço? Para visitar a Via Láctea.",
    "Sabe por que o livro de matemática se matou? Porque ele tinha muitos problemas.",
    "Por que o Windows vive triste? Porque tem muitas janelas fechadas.",
    "Por que o Wi-Fi terminou com a tomada? Porque ela vivia dando choque nele.",
    "Por que o celular foi ao médico? Porque ele estava com vírus.",
    "Qual é o cúmulo do egoísmo? Não doar sangue porque é do tipo ‘O+’ (ô mais eu)."
]

def piada_aleatoria():
    return random.choice(piadas)
