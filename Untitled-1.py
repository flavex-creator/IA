
a = 19.4
b = 18.6
c = 17


print(type(c))


"""Conversão implícita do tipo de dados da variável c, devido ao resultado da operação"""

# A operação envolve floats (a e b), então c será convertido implicitamente para float
c = (c + b + a) / 3

# Mostra o resultado e o novo tipo de c
print(c)
print(type(c))
