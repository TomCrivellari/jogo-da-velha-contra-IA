def marcar_jogada(jogada, tabela_jogo, simbolo):
    if jogada == 1:
        tabela_jogo[0][0] = simbolo
    else:
        if jogada == 2:
            tabela_jogo[0][1] = simbolo
        else:
            if jogada == 3:
                tabela_jogo[0][2] = simbolo
            else:
                if jogada == 4:
                    tabela_jogo[1][0] = simbolo
                else:
                    if jogada == 5:
                        tabela_jogo[1][1] = simbolo
                    else:
                        if jogada == 6:
                            tabela_jogo[1][2] = simbolo
                        else:
                            if jogada == 7:
                                tabela_jogo[2][0] = simbolo
                            else:
                                if jogada == 8:
                                    tabela_jogo[2][1] = simbolo
                                else:
                                    tabela_jogo[2][2] = simbolo
    return tabela_jogo
                        
def verificar_se_a_posição_esta_vazia(jogada, tabela_jogo, posicao_vazia):
    if jogada == 1:
        if tabela_jogo[0][0] == "_":
            posicao_vazia = 1
    else:
        if jogada == 2:
            if tabela_jogo[0][1] == "_":
                posicao_vazia = 1
        else:
            if jogada == 3:
                if tabela_jogo[0][2] == "_":   
                    posicao_vazia = 1
            else:
                if jogada == 4:
                    if tabela_jogo[1][0] == "_":        
                        posicao_vazia = 1
                else:
                    if jogada == 5:
                        if tabela_jogo[1][1] == "_":            
                            posicao_vazia = 1
                    else:
                        if jogada == 6:
                            if tabela_jogo[1][2] == "_":
                                posicao_vazia = 1
                        else:
                            if jogada == 7:
                                if tabela_jogo[2][0] == "_":
                                    posicao_vazia = 1
                            else:
                                if jogada == 8:
                                    if tabela_jogo[2][1] == "_":
                                        posicao_vazia = 1
                                else:
                                    if tabela_jogo[2][2] == "_":
                                        posicao_vazia = 1
    return posicao_vazia
                                            
def verificar_vitoria(tabela_jogo, final):
    if (tabela_jogo[0][0] == tabela_jogo[0][1] == tabela_jogo[0][2]) and tabela_jogo[0][0] != "_":
        final = 1
    else:
        if (tabela_jogo[1][0] == tabela_jogo[1][1] == tabela_jogo[1][2]) and tabela_jogo[1][0] != "_":
            final = 1
        else:
            if (tabela_jogo[2][0] == tabela_jogo[2][1] == tabela_jogo[2][2]) and tabela_jogo[2][0] != "_":
                final = 1
            else:
                if (tabela_jogo[0][0] == tabela_jogo[1][0] == tabela_jogo[2][0]) and tabela_jogo[0][0] != "_":
                    final = 1
                else:
                    if (tabela_jogo[0][1] == tabela_jogo[1][1] == tabela_jogo[2][1]) and tabela_jogo[0][1] != "_":
                        final = 1
                    else:
                        if (tabela_jogo[0][2] == tabela_jogo[1][2] == tabela_jogo[2][2]) and tabela_jogo[0][2] != "_":
                            final = 1
                        else:
                            if (tabela_jogo[0][0] == tabela_jogo[1][1] == tabela_jogo[2][2]) and tabela_jogo[0][0] != "_":
                                final = 1
                            else:
                                if (tabela_jogo[0][2] == tabela_jogo[1][1] == tabela_jogo[2][0]) and tabela_jogo[0][2] != "_":
                                    final = 1
                                else:
                                    final = 0
    return final

def verificar_empate(tabela_jogo):
    cont = 0
    for i in range(len(tabela_jogo)):
        for j in range(len(tabela_jogo[i])):
            if tabela_jogo[i][j] != "_":
                cont += 1
    return cont

def primeira_jogada_IA(jogada):
    if jogada == 1:
        jogada_IA = 5
    else:
        if jogada == 2:
            jogada_IA = 3
        else:
            if jogada == 3:
                jogada_IA = 5
            else:
                if jogada == 4:
                    jogada_IA = 1
                else:
                    if jogada == 5:
                        jogada_IA = 1
                    else:
                        if jogada == 6:
                            jogada_IA = 3
                        else:
                            if jogada == 7:
                                jogada_IA = 5
                            else:
                                if jogada == 8:
                                    jogada_IA = 9
                                else:
                                    if jogada == 9:
                                        jogada_IA = 5
    return jogada_IA

def segunda_jogada_IA(tabela_jogo):
    if "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 3
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9 #vitoria
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9 #vitoria
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 5
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 5

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3 #vitoria
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 3 #vitoria
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3

    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1

    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8
        
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 3 #vitoria
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3 #vitoria

    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7
    return jogada_IA

def terceira_jogada_IA(tabela_jogo):
    if "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim

    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8#fim

    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3#fim

    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6#fim

    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7

    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3#fim

    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8#fim




    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9#vitoria
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5#vitoria
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6#fim

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7#vitoria
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6#fim

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8 
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim




    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8#fim

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 1#fim

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4#fim

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4#fim

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1#fim

    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6




    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3#vitoria
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3
    
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9#vitoria
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2#fim

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5#vitoria
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2#fim




    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7#vitoria
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4
    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4#fim
    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2
    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3#fim
    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7#fim
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5#vitoria
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7#vitoria
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6#fim
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8#fim
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1#fim
    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6#fim
    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1#fim
    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1#fim
    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5#vitoria
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6#fim
    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][3]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3

    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1#fim
    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1#vitoria
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6#fim
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4#fim
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 3#fim
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7#fim
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2#fim
    
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 3#fim
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3#fim
    
    return jogada_IA

def quarta_jogada_IA(tabela_jogo):
    if "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6


    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6


    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3


    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6


    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6
    

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1

    
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 1


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 1


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 5
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 5


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6
    

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1
    

    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4


    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 3


    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8
    

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2
    

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2


    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    

    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 6


    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7

    
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8

    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 3

    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2


    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 6

    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 4

    
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6

    

    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2

    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 8
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 2


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 1


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8

    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 7

    
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 5
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 4
    elif "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[2][1]:
        jogada_IA = 4


    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 9
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][2]:
        jogada_IA = 8


    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3

    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 1


    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][2]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2
    

    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 9
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 9
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[2][2]:
        jogada_IA = 3

    
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 2
    

    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][0] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][2] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3


    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4

    
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4


    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 1
    

    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 6


    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4


    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][2]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 3
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[2][0]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][1] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2]:
        jogada_IA = 1


    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 4


    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[0][1]:
        jogada_IA = 5
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][0]:
        jogada_IA = 5
    elif "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][0] and "X" in tabela_jogo[1][1]:
        jogada_IA = 2
    

    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 7
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][0] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][2]:
        jogada_IA = 4


    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][0]:
        jogada_IA = 8
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[0][1] and "X" in tabela_jogo[2][1]:
        jogada_IA = 7


    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][0] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[2][1]:
        jogada_IA = 2


    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][0]:
        jogada_IA = 2
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1]:
        jogada_IA = 1
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[1][2] and "O" in tabela_jogo[0][2] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[1][0]:
        jogada_IA = 2

    

    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][0]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[0][2]:
        jogada_IA = 6
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][0] and "O" in tabela_jogo[2][1] and "X" in tabela_jogo[0][1] and "O" in tabela_jogo[1][0] and "X" in tabela_jogo[1][2]:
        jogada_IA = 3
    

    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][0]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[0][1]:
        jogada_IA = 4
    elif "X" in tabela_jogo[2][2] and "O" in tabela_jogo[1][1] and "X" in tabela_jogo[2][1] and "O" in tabela_jogo[2][0] and "X" in tabela_jogo[0][2] and "O" in tabela_jogo[1][2] and "X" in tabela_jogo[1][0]:
        jogada_IA = 1

    
    return jogada_IA

tabela_jogo = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

final = 0
ganhador = 0
jogada_IA = 0

print("Tabela do jogo: ")
for i in range(3):
    print(tabela_jogo[i])
print("\n")

while final == 0:
    simbolo = 'X'
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

    simbolo = 'O'
    jogada_IA += 1
    #Jogada IA
    if jogada_IA == 1:
        jogada = primeira_jogada_IA(jogada)
        tabela_jogo = marcar_jogada(jogada, tabela_jogo, simbolo)
    else:
        if jogada_IA == 2:
            jogada = segunda_jogada_IA(tabela_jogo)
            tabela_jogo = marcar_jogada(jogada, tabela_jogo, simbolo)
        else:
            if jogada_IA == 3:
                jogada = terceira_jogada_IA(tabela_jogo)
                tabela_jogo = marcar_jogada(jogada, tabela_jogo, simbolo)
            else:
                if jogada_IA == 4:
                    jogada = quarta_jogada_IA(tabela_jogo)
                    tabela_jogo = marcar_jogada(jogada, tabela_jogo, simbolo)


    final = verificar_vitoria(tabela_jogo, final)
    if final == 1:
        ganhador = 1
    
    contador_de_casas = verificar_empate(tabela_jogo)
    if contador_de_casas == 9:
        final = 1
        ganhador = 2

    print("Tabela do jogo: ")
    for i in range(3):
        print(tabela_jogo[i])


print("Fim de Jogo!!")
if ganhador == 2:
    print("Deu Velha (empate)")
else:
    print(f"O Computador é o vencedor!")