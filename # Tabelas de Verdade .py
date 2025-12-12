# Tabelas de Verdade (Operadores Lógicos: and, or, not)

print("-- TABELA DE VERDADE - OP. LÓG. AND --")
print("A\tB\t\tA and B")
# Operador AND (Conjunção)
# A tabela de verdade do operador AND é verdadeira somente quando ambas as condições são verdadeiras.
a = b = True
print(a, "\t", b, "\t\t", a and b)

a = True
b = False
print(a, "\t", b, "\t\t", a and b)

a = False
b = True
print(a, "\t", b, "\t\t", a and b)

a = b = False
print(a, "\t", b, "\t\t", a and b)

# Separação entre tabelas de operadores
print("\n-- TABELA DE VERDADE - OP. LÓG. OR --")

# Operador OR (Disjunção)
# A tabela de verdade do operador OR é verdadeira quando pelo menos uma das condições é verdadeira.
a = b = True
print(a, "\t", b, "\t\t", a or b)

a = True
b = False
print(a, "\t", b, "\t\t", a or b)

a = False
b = True
print(a, "\t", b, "\t\t", a or b)

a = b = False
print(a, "\t", b, "\t\t", a or b)

# Separação entre tabelas de operadores
print("\n-- TABELA DE VERDADE - OP. LÓG. NOT --")
print("A\t\tnot(a)")
# Operador NOT (Negação)
# O operador NOT inverte o valor lógico da expressão.
a = True
print(a, "\t\t", not a)

a = False
print(a, "\t\t", not a)
