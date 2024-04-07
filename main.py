import tkinter as tk
from velhaIA import playVeia

janela = tk.Tk()
janela.geometry('400x400')

branco = "#FFFFFF"  # branca / white
preto = "#333333"  # preta pesado / dark black
laranja = "#fcc058"  # laranja / orange
valor = "#38576b"  # valor / value
azul = "#3297a8"   # azul / blue
amarelo = "#fff873"   # amarela / yellow
vermelho = "#e85151"   # vermelha / red
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black



jogando = 'X'
tabela = [1,2,3,
          4,5,6,
          7,8,9]

def iniciar_jogo(IA):
    global botao_1,botao_2,botao_3,botao_4,botao_5,botao_6,botao_7,botao_8,botao_9,botoes
    # Definindo os botões (quadrados)
    class Botao:
        def __init__(self,n):
            self.botao = tk.Button(janela,text='',font=('Ivy 50 bold'),overrelief='ridge',relief='flat',width=3,bg=branco,fg=vermelho)

    botao_1 = Botao(0).botao
    botao_2 = Botao(1).botao
    botao_3 = Botao(2).botao
    botao_4 = Botao(3).botao
    botao_5 = Botao(4).botao
    botao_6 = Botao(5).botao
    botao_7 = Botao(6).botao
    botao_8 = Botao(7).botao
    botao_9 = Botao(8).botao

    botoes = [botao_1,botao_2,botao_3,botao_4,botao_5,botao_6,botao_7,botao_8,botao_9]

    # Posição dos botões
    botao_1.place(x=0,y=2)
    botao_2.place(x=133,y=2)
    botao_3.place(x=266,y=2)
    botao_4.place(x=0,y=135)
    botao_5.place(x=133,y=135)
    botao_6.place(x=266,y=135)
    botao_7.place(x=0,y=270)
    botao_8.place(x=133,y=270)
    botao_9.place(x=266,y=270)

    botao_1['command'] = lambda:play(0,IA)
    botao_2['command'] = lambda:play(1,IA)
    botao_3['command'] = lambda:play(2,IA)
    botao_4['command'] = lambda:play(3,IA)
    botao_5['command'] = lambda:play(4,IA)
    botao_6['command'] = lambda:play(5,IA)
    botao_7['command'] = lambda:play(6,IA)
    botao_8['command'] = lambda:play(7,IA)
    botao_9['command'] = lambda:play(8,IA)

    # Linhas horizontais
    label = tk.Label(janela,width=400,font=('Ivy 1 bold'),bg=preto)
    label.place(y=133)

    label = tk.Label(janela,width=400,font=('Ivy 1 bold'),bg=preto)
    label.place(y=266)

    # Linhas verticais
    label = tk.Label(janela,height=200,anchor='center',font=('Ivy 1 bold'),bg=preto)
    label.place(x=133)

    label = tk.Label(janela,height=200,font=('Ivy 1 bold'),anchor='center',bg=preto)
    label.place(x=266)


# Fazer determindada jogada
def play(n,IA):
    global jogando,tabela

    # Se o quadrado já tiver sido jogado, ignorar
    if isinstance(tabela[n],str):
        return
    
    # Atualizar tabela
    tabela[n] = jogando

    # Atualizar texto do botão
    botao = botoes[n]
    botao['text'] = jogando

    # Cor do texto 
    if jogando == 'X':
        botao['fg'] = vermelho
        jogando = 'O'
    else:
        botao ['fg'] = azul
        jogando = 'X'
    
    # Se o jogo ainda não tiver acabado, for contra IA e vez do 'O', então IA joga
    vencedor = get_winner(tabela)
    if vencedor:
        fim_jogo(vencedor)
    elif IA and jogando == 'O':
        jogada = playVeia(tabela) - 1
        play(jogada,tabela)

def get_winner(tab):
    global jogando

    # Linhas, Colunas e Diagonais
    lcd = [tab[:3],tab[3:6],tab[6:],
            tab[:7:3],tab[1:8:3],tab[2::3],
            tab[::4],tab[2:7:2]]

    # Verificar se uma linha/coluna/diagonal tem 3 'X' ou 3 'O'
    for opcao in lcd:
        conj = set(opcao)
        if len(conj) == 1:
            winner = list(conj)[0]
            return fim_jogo(winner)
    if all(isinstance(quad,str) for quad in tabela):
        return fim_jogo('empate')

def fim_jogo(vencedor):
    global venc,botao_jogar_novamente_ia,botao_jogar_novamente_jogadores
    
    venc = tk.Label(janela,font=('Ivy 30 bold'),bg=fundo,fg=branco)
    if vencedor == 'X':
        venc['text'] = 'Vencedor: X'
        venc.place(x=100,y=120)
    elif vencedor=='O':
        venc['text'] = 'Vencedor: O'
        venc.place(x=100,y=120)
    elif vencedor=='empate':
        venc['text'] = 'Empate'
        venc.place(x=130,y=120)
    
    # Posição dos botões jogar novamente
    botao_jogar_novamente_jogadores = tk.Button(janela,command=lambda:reiniciar(False),bg=fundo,fg=branco,text='Jogar novamente: 2 jogadores',font=('Ivy 10 bold'))
    botao_jogar_novamente_ia = tk.Button(janela,command=lambda:reiniciar(True),bg=fundo,fg=branco,text='Jogar novamente: computador',font=('Ivy 10 bold'))
    botao_jogar_novamente_jogadores.place(x=110,y=230)
    botao_jogar_novamente_ia.place(x=110,y=260)

    return vencedor

def reiniciar(IA):
    global jogando,tabela
    jogando = 'X'
    tabela = [1,2,3,4,5,6,7,8,9]
    
    for widget in janela.winfo_children():
        widget.destroy()

    iniciar_jogo(IA)


# Botão para jogar entre 2 jogadores
botao_2_jogardores = tk.Button(janela,command=lambda:iniciar_jogo(False),bg=fundo,text='2 jogadores',fg=branco)
botao_2_jogardores.place(x=100,y=150)

# Botão para jogar contra IA
botao_vs_ia = tk.Button(janela,command=lambda:iniciar_jogo(True),bg=fundo,text='Computador',fg=branco)
botao_vs_ia.place(x=200,y=150)



tk.mainloop()