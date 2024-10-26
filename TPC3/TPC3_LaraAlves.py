def jogo_dos_fosforos():
    def jogada_usuario(fosforos):
        while True:
            try:
                jogada = int(input(f"Há {fosforos} fósforos. Quantos fósforos quer tirar? (1-4): "))
                if jogada < 1 or jogada > 4 or jogada > fosforos:
                    print("Jogada inválida! Deve escolher entre 1 e 4 fósforos, e não mais do que os fósforos restantes.")
                else:
                    return jogada
            except ValueError:
                print("Por favor, insira um número válido entre 1 e 4.")

    def jogada_computador(fosforos):
        jogada = (fosforos - 1) % 5
        if jogada == 0:
            jogada = 1
        print(f"O computador tira {jogada} fósforos.")
        return jogada

    def verifica_vencedor(fosforos, jogador):
        if fosforos == 0:
            if jogador == "utilizador":
                print("O utilizador tirou o último fósforo. O utilizador perde!")
            else:
                print("O computador tirou o último fósforo. O computador perde!")
            return True
        return False

    def jogo():
        fosforos = 21
        modo = int(input("Escolha o modo de jogo (1- Jogador começa, 2- Computador começa): "))
        
        if modo not in [1, 2]:
            print("Modo inválido! Escolha 1 ou 2.")
            return
        
        turno = "utilizador" if modo == 1 else "computador"
        jogo_terminado = False

        while not jogo_terminado:
            if turno == "utilizador":
                fosforos -= jogada_usuario(fosforos)
                jogo_terminado = verifica_vencedor(fosforos, "utilizador")
                turno = "computador"
            else:
                fosforos -= jogada_computador(fosforos)
                jogo_terminado = verifica_vencedor(fosforos, "computador")
                turno = "utilizador"