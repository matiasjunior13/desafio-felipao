vitorias = 53
derrotas = 5


def calcular_nivel(vitorias, derrotas):
    saldo = vitorias - derrotas
    
    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return f"O Herói tem saldo de {saldo} está no nível de {nivel}"

resultado = calcular_nivel(vitorias, derrotas)
print(resultado)

