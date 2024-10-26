import random

def criar_lista_aleatoria():
    tamanho = int(input("Quantos números deseja na lista? "))
    return [random.randint(1, 100) for _ in range(tamanho)]

def ler_lista():
    lista = []
    tamanho = int(input("Quantos números deseja adicionar à lista? "))
    for _ in range(tamanho):
        num = int(input("Introduza um número: "))
        lista.append(num)
    return lista

def soma_lista(lista):
    return sum(lista)

def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0

def maior_elemento(lista):
    return max(lista) if lista else None

def menor_elemento(lista):
    return min(lista) if lista else None

def esta_ordenada_crescente(lista):
    return lista == sorted(lista)

def esta_ordenada_decrescente(lista):
    return lista == sorted(lista, reverse=True)

def procura_elemento(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1

def mostrar_menu():
    print("\nMenu:")
    print("(1) Criar Lista Aleatória")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está Ordenada por Ordem Crescente?")
    print("(8) Está Ordenada por Ordem Decrescente?")
    print("(9) Procurar um Elemento")
    print("(0) Sair")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            lista = criar_lista_aleatoria()
            print(f"Lista criada: {lista}")
        elif opcao == 2:
            lista = ler_lista()
            print(f"Lista lida: {lista}")
        elif opcao == 3:
            print(f"Soma dos elementos: {soma_lista(lista)}")
        elif opcao == 4:
            print(f"Média dos elementos: {media_lista(lista)}")
        elif opcao == 5:
            print(f"Maior elemento: {maior_elemento(lista)}")
        elif opcao == 6:
            print(f"Menor elemento: {menor_elemento(lista)}")
        elif opcao == 7:
            print(f"Está ordenada por ordem crescente? {'Sim' if esta_ordenada_crescente(lista) else 'Não'}")
        elif opcao == 8:
            print(f"Está ordenada por ordem decrescente? {'Sim' if esta_ordenada_decrescente(lista) else 'Não'}")
        elif opcao == 9:
            elemento = int(input("Introduza o número a procurar: "))
            posicao = procura_elemento(lista, elemento)
            if posicao == -1:
                print(f"O elemento {elemento} não está na lista.")
            else:
                print(f"O elemento {elemento} está na posição {posicao}.")
        elif opcao == 0:
            print(f"Sair. Lista final: {lista}")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()