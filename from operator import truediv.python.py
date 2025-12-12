# Atribuição de dados a variáveis, ficando automaticamente declaradas
i = 90
f = 1.5
c = 2 + 3j
disc = "APIB"
l = "True"
d = [1.5, 12, "AIB"]
e = (7, "Classif", 19.6)
cc = {1, 2, 3, 4, 5, 6}
dic = {
    1: 'decimo',
    2: 'decimo primeiro',
    3: 'decimo segundo'
}

# Utilização da função Type na determinação do tipo de dado de cada variável
td = type(i)
print(td)
td = type(f)
print(td)
td = type(c)
print(td)
st = type(disc)
print(st)
st = type(l)
print(st)
st = type(d)
print(st)
st = type(e)
print(st)
st = type(cc)
print(st)
st = type(dict)
print(st)

# Imp imprimir uma linha de separação
print("---------------")

# Utilização da função Type na determinação do tipo de dado de cada valor
st = type(3.14)
print(st)
st = type(9999)
print(st)
