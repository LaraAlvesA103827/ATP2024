print("1-Queres adivinhar um número ou 2-que eu adivinhe o teu?")
modo=int(input("1 ou 2?"))
if modo ==(1):
    import random
    d = random.randrange(1,100)
    t = 1
    x = int(input("Diga um número"))
    while d!=x:
        t = t + 1
        if d>x:
            print("maior que " + str(x),flush=True)
        else:
            print("menor que " + str(x),flush=True)
        x =  int(input("Diga um número"))        
        
    print("Acertou em ", t , "tentativas!")
    


if modo == (2):
    sup = 100
    inf = 0
    x = 0
    n = 0
    pergunta=str()
    acertou = str("acertou")
    while pergunta!=str(acertou):
        n = n + 1
        x = int((sup + inf) / 2)
        pergunta = input("O seu número é " + str(x)+"?")
        if pergunta == "maior":
            inf = x
        else:
            sup = x
    print("Acertei o número em " + str(n) + " tentativas")