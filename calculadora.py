import math

# Funções matemáticas seguras
funcoes_permitidas = {
    "sqrt": math.sqrt,
    "log": math.log,
    "ln": math.log,
    "log10": math.log10,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round,
    "pow": pow
}

def resolver_expressao(expressao):
    try:
        expressao = expressao.replace("^", "**")  # permite 2^3
        resultado = eval(expressao, {"__builtins__": None}, funcoes_permitidas)
        return f"O resultado é: {resultado}"
    except Exception as e:
        return f"Não consegui resolver. Verifique a expressão. Detalhes: {str(e)}"
