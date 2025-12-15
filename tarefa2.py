LInf = int(input("Digite o limite inferior: "))
LSup = int(input("Digite o limite superior: "))

if LInf < LSup:
    for i in range( LInf, LSup + 1):
        print(i)
else:
    print('Os limites indicados para o intervalo estão errados.')

   