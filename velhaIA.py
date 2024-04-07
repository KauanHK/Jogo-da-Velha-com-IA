from itertools import permutations

def playVeia(tabela):

    def play(tab,jog,jogando):
        indice = jog - 1
        tab[indice] = jogando
        return tab

    def get_winner(tab):
        # Linhas, Colunas e Diagonais
        lcd = [tab[:3],tab[3:6],tab[:6],
            tab[:7:3],tab[1:8:3],tab[2::3],
            tab[::4],tab[2:7:2]]
        
        for opcao in lcd:
            if len(set(opcao)) == 1:
                winner = list(set(opcao))[0]
                return winner
        if all(isinstance(i,str) for i in tab):
            return "empate"
        return False

    def ia_play(tab):


        def definir_jogada(tab,start,end,interval):
            for espaco in tab[start:end:interval]:
                if isinstance(espaco,int):
                    return espaco

        def can_win(tab):

            if tab.count("O") < 2:
                return False
            
            lcd = [(tab[:3],[None,3,None]), (tab[3:6],[3,6,None]),(tab[:6],[6,None,None]),
            (tab[:7:3],[None,7,3]),(tab[1:8:3],[1,8,3]),(tab[2::3],[2,None,3]),
            (tab[::4],[None,None,4]),(tab[2:7:2],[2,7,2])]
            
            for opcao in lcd:
                if opcao[0].count("O") == 2 and "X" not in opcao[0]:
                    s,e,i = opcao[1]
                    jogada = definir_jogada(tab,s,e,i)
                    return jogada
            return False
            
        def can_lose(tab):
            if tab.count("X") < 2:
                return False
            
            lcd = [(tab[:3],[None,3,None]), (tab[3:6],[3,6,None]),(tab[6:],[6,None,None]),
            (tab[:7:3],[None,7,3]),(tab[1:8:3],[1,8,3]),(tab[2::3],[2,None,3]),
            (tab[::4],[None,None,4]),(tab[2:7:2],[2,7,2])]
            
            for opcao in lcd:
                if opcao[0].count("X") == 2 and "O" not in opcao[0]:
                    s,e,i = opcao[1]
                    jogada = definir_jogada(tab,s,e,i)
                    return jogada
            return False

            
        jogada = can_win(tab)
        if not jogada:
            jogada = can_lose(tab)
        if not jogada:

            cantos_opostos = [(tabela[::8] == ['X','X']),(tabela[2:7:5] == ['X','X'])]
            meio = tabela[4] == 'X'
            canto = [tabela[0] == 'X',tabela[2] == 'X',tabela[6] == 'X',tabela[8] == 'X']
            if any(cantos_opostos) and tab.count("X") == 2:
                jogada = 2
                return jogada
            elif meio and any(canto) and tabela.count('X') == 2:
                jogada = 3
                return jogada

            #Todas as permutacoes das sequencias de jogadas possiveis
            jogadas_disponiveis = [n for n in tab if isinstance(n,int)]
            permutacoes = list(permutations(jogadas_disponiveis))

            # Simular todos os jogos possíveis com cada permutação
            winners = []
            first_plays = []
            for permutacao in permutacoes:
                simulador = tab[:]
                jogando = 'O'
                for jog in permutacao:
                    simulador = play(simulador,jog,jogando)
                    winner = get_winner(simulador)
                    if winner:
                        break
                    jogando = 'O' if jogando == 'X' else 'X'
                first_plays.append(permutacao[0])
                winners.append(winner)
            
            # First plays que 'O' terminou como vencedor
            fp_winners = [fp for i,fp in enumerate(first_plays) if winners[i] == 'O']

            # Identificar qual jogada que mais se repetiu
            conjunto_fp = set(fp_winners)
            max = 0
            for fp in conjunto_fp:
                repeticoes = fp_winners.count(fp)
                if repeticoes > max:
                    jogada = fp
                    max = repeticoes

        return jogada
            

    jogada = ia_play(tabela)
    return jogada


    # tabela = play(tabela,jogada,"O")
    # print(tabela[:3])
    # print(tabela[3:6])
    # print(tabela[6:])