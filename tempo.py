seg= int(input("Digite os segundos: "))
min= int(input("Digite os minutos: "))
horas= int(input("Digite as horas: "))

if (seg<60) and (seg>=1) and (min>=0) and (min<60) and (horas>=0):
    res=int(seg + min*60 + horas*3600)
    print("digite o valor dos segundos totais: ",res)
else:
    print("valor inválido")