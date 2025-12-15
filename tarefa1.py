LInf = int(input("Digite o limite inferior: "))
LSup = int(input("Digite o limite superior: "))

while  LInf> LSup:
    print("Os limites indicados para o intervalo estão errados.")
    LInf = int(input("Digite o limite inferior: "))
    LSup = int(input("Digite o limite superior: "))

while LInf <= LSup:
        print("iteração numero: ", LInf)
        LInf= LInf + 1


