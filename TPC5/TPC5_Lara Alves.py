sala1=[50,[],"Twilight"]
sala2=[60,[],"Barbie"]
sala3=[75,[],"Harry Potter"]
sala4=[45,[],"Princesa e o sapo"]
cinema=[sala1,sala2,sala3,sala4]

def listar(cinema):
    k = 1
    for sala in cinema:
        print("sala" + str(k) + ": " + sala[2], flush = True)
        k = k + 1  
    return

def disponível(cinema, filme, lugar):
    res = False
    for sala in cinema:
        if filme == sala[2]:
            if lugar not in sala[1]:
                res = True
    return res

def vendeBilhete( cinema, filme, lugar ):
    if disponível(cinema, filme, lugar):
        for sala in cinema:
            if filme==sala[2]:
                sala[1].append(lugar)
                print("O lugar " + str(lugar) + " foi reservado com sucesso.", flush = True)
    else:
        print("O lugar que escolheu não está disponível.")
    return cinema

def listardisponibilidades( cinema ):
    l = []
    for sala in cinema:
        info = (sala[2], sala[0] - len(sala[1]))
        l.append(info)
    return l

def inserirSala( cinema, lotação, filme):
    sala=[lotação,[],filme]
    if sala not in cinema:
        cinema.append(sala)
    print("A sala foi adicionada com sucesso!")
    
menu =print(
"""Bom dia! Obrigado por escolher o nosso Cinema, aqui estão os comandos quue pode realizar: 
(0) Fechar o menu.
(1) Listar todos os filmes em exibição;
(2) Verificar a disponibilidade da sala e do lugar;
(3) Comprar bilhete, somente após verificar a disponibilidade;
(4) Listar os lugares restantes em cada sala
(5) Inserir uma nova sala de exibição""")

opc = -1  
while opc != 0:
    opc = int(input("Selecione a opção do menu que pretende efetuar! Se quiser encerrar o menu, selecione a opção 6."))
    if opc == 1:
        listar(cinema)

    elif opc == 2:
        print(disponível(cinema,input("Escolhe o filme que queres ver"),int(input("Escolhe um lugar da sala"))))

    elif opc == 3:
       vendeBilhete(cinema,input("Escolhe o filme que queres ver"),input("Escolhe o lugar em que queres ver o filme"))

    elif opc == 4:
        print(listardisponibilidades(cinema), flush = True)
    
    elif opc == 5:
        inserirSala(cinema,int(input("Qual a lotação da sala?")),input(("Qual o filme em exibição?")))

print("Muito Obrigado! Volte Sempre.")