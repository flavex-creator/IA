

def adicao(n1, n2):
    adicao=0
    adicao=n1+n2
    return adicao

def multiplicacao(n1, n2):
    multiplicacao=0
    multiplicacao=n1+n2
    return multiplicacao




n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
opcao = input("Escolha uma operação adicao (A) ou multiplicacao(M): ")



if opcao == "A":
    print("Resultado da Adição:", adicao(n1, n2))

else:
     print("Resultado da Multiplicação:", multiplicacao(n1, n2))




