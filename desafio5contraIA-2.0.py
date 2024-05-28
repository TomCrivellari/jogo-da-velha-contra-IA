coordenadas = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

def marcar_jogada(jogada, tabela_jogo, simbolo):
    tabela_jogo[coordenadas[jogada-1][0]][coordenadas[jogada-1][1]] = simbolo
    return tabela_jogo

def verificar_se_a_posição_esta_vazia(jogada, tabela_jogo, posicao_vazia):
    if tabela_jogo[coordenadas[jogada-1][0]][coordenadas[jogada-1][1]] == "_":
        posicao_vazia = 1
    return posicao_vazia

def verificar_vitoria(tabela_jogo, final, simbolo):
    contador = 0
    for i in range(len(tabela_jogo)):
        for j in range(len(tabela_jogo)):
            if tabela_jogo[i][j] == simbolo:
                contador += 1
        if contador == 3:
            final = 1
        contador = 0
    for i in range(len(tabela_jogo)):
        for j in range(len(tabela_jogo)):
            if tabela_jogo[j][i] == simbolo:
                contador += 1
        if contador == 3:
            final = 1
        contador = 0
    for i in range(len(tabela_jogo)):
        if tabela_jogo[i][i] == simbolo:
            contador += 1
    if contador == 3:
        final = 1
    contador = 0
    for i in range(len(tabela_jogo)):
        if tabela_jogo[i][len(tabela_jogo)-1-i] == simbolo:
            contador += 1
    if contador == 3:
        final = 1
    return final

def verificar_empate(tabela_jogo, final):
    cont = 0
    for i in range(len(tabela_jogo)):
        for j in range(len(tabela_jogo[i])):
            if tabela_jogo[i][j] != "_":
                cont += 1
    return cont

def verificar_vitoria_IA(tabela_jogo, simbolo):
    contador = 0
    verificar_jogada_IA = 0
    for i in range(len(tabela_jogo)):
        for j in range(len(tabela_jogo)):
            if tabela_jogo[i][j] == simbolo:
                contador += 1
        if contador == 2:
            for j in range(len(tabela_jogo)):
                if tabela_jogo[i][j] == "_":
                    tabela_jogo[i][j] = simbolo
                    verificar_jogada_IA = 1
        contador = 0
    if verificar_jogada_IA == 0:
        for i in range(len(tabela_jogo)):
            for j in range(len(tabela_jogo)):
                if tabela_jogo[j][i] == simbolo:
                    contador += 1
            if contador == 2:
                for j in range(len(tabela_jogo)):
                    if tabela_jogo[j][i] == "_":
                        tabela_jogo[j][i] = simbolo
                        verificar_jogada_IA = 1
            contador = 0
        if verificar_jogada_IA == 0:
            for i in range(len(tabela_jogo)):
                if tabela_jogo[i][i] == simbolo:
                    contador += 1
            if contador == 2:
                for i in range(len(tabela_jogo)):
                    if tabela_jogo[i][i] == "_":
                        tabela_jogo[i][i] = simbolo
                        verificar_jogada_IA = 1
            contador = 0
            if verificar_jogada_IA == 0:
                for i in range(len(tabela_jogo)):
                    if tabela_jogo[i][len(tabela_jogo)-1-i] == simbolo:
                        contador += 1
                if contador == 2:
                    for i in range(len(tabela_jogo)):
                        if tabela_jogo[i][len(tabela_jogo)-1-i] == "_":
                            tabela_jogo[i][len(tabela_jogo)-1-i] = simbolo
                            verificar_jogada_IA = 1
    return tabela_jogo, verificar_jogada_IA

def verificar_vitoria_jogador(tabela_jogo, simbolo):
    contador = 0
    verificar_jogada_IA = 0
    for i in range(len(tabela_jogo)):
        for j in range(len(tabela_jogo)):
            if tabela_jogo[i][j] == "X":
                contador += 1
        if contador == 2:
            for j in range(len(tabela_jogo)):
                if tabela_jogo[i][j] == "_":
                    tabela_jogo[i][j] = simbolo
                    verificar_jogada_IA = 1
        contador = 0
    if verificar_jogada_IA == 0:
        for i in range(len(tabela_jogo)):
            for j in range(len(tabela_jogo)):
                if tabela_jogo[j][i] == "X":
                    contador += 1
            if contador == 2:
                for j in range(len(tabela_jogo)):
                    if tabela_jogo[j][i] == "_":
                        tabela_jogo[j][i] = simbolo
                        verificar_jogada_IA = 1
            contador = 0
        if verificar_jogada_IA == 0:
            for i in range(len(tabela_jogo)):
                if tabela_jogo[i][i] == "X":
                    contador += 1
            if contador == 2:
                for i in range(len(tabela_jogo)):
                    if tabela_jogo[i][i] == "_":
                        tabela_jogo[i][i] = simbolo
                        verificar_jogada_IA = 1
            contador = 0
            if verificar_jogada_IA == 0:
                for i in range(len(tabela_jogo)):
                    if tabela_jogo[i][len(tabela_jogo)-1-i] == "X":
                        contador += 1
                if contador == 2:
                    for i in range(len(tabela_jogo)):
                        if tabela_jogo[i][len(tabela_jogo)-1-i] == "_":
                            tabela_jogo[i][len(tabela_jogo)-1-i] = simbolo
                            verificar_jogada_IA = 1
    return tabela_jogo, verificar_jogada_IA

def marcar_jogada_IA_aleatoria(tabela_jogo, simbolo):
    verificar_jogada_IA = 0
    i = 0
    j = 0
    while verificar_jogada_IA == 0:
        while verificar_jogada_IA == 0:
            if tabela_jogo[i][j] == "_":
                tabela_jogo[i][j] = simbolo
                verificar_jogada_IA = 1
            j += 1
        i += 1
    return tabela_jogo

tabela_jogo = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

final = 0
vitoria = 0
ganhador = 0
simbolo = "O"

print("Tabela do jogo: ")
for i in range(3):
    print(tabela_jogo[i])
print("\n")

while final == 0:
    if simbolo == "O":
        simbolo = "X"
        print("Vez do X: ")
        jogada = int(input("Digite sua jogada (de 1 a 9 referente ao quadrante da jogada): "))
        verificacao = 0
        posicao_vazia = 0
        while verificacao == 0:
            if jogada < 1 or jogada > 9:
                jogada = int(input("Jogada Invalida (digite um numero 1 a 9 referente ao quadrante da jogada): "))
            else:
                posicao_vazia = verificar_se_a_posição_esta_vazia(jogada, tabela_jogo, posicao_vazia)
                if posicao_vazia != 1:
                    jogada = int(input("Jogada Invalida (Essa jogada ja foi escolhida anteriormente, escolha outra de 1 a 9): "))
                else:
                    verificacao = 1
        tabela_jogo = marcar_jogada(jogada, tabela_jogo, simbolo)
        final = verificar_vitoria(tabela_jogo, final, simbolo)
    else:
        simbolo = "O"
        verificar_jogada_IA = 0
        tabela_jogo, verificar_jogada_IA = verificar_vitoria_IA(tabela_jogo, simbolo)
        if verificar_jogada_IA == 0:
            tabela_jogo, verificar_jogada_IA = verificar_vitoria_jogador(tabela_jogo, simbolo)
            if verificar_jogada_IA == 0:
                tabela_jogo = marcar_jogada_IA_aleatoria(tabela_jogo,simbolo)
        
        final = verificar_vitoria(tabela_jogo, final, simbolo)

    if final == 0:
        contador_de_casas = verificar_empate(tabela_jogo, final)
        if contador_de_casas == 9 and vitoria != 1:
            final = 1
            ganhador = 3
    
    print("Tabela do jogo: ")
    for i in range(3):
        print(tabela_jogo[i])

print("Fim de Jogo!!")
if ganhador == 3:
    print("Deu Velha (empate)")
else:
    print(f"O jogador {simbolo} é o vencedor!")