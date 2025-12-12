# Demonstração dos operadores aritméticos

b = int(input("Indique o valor de um número: "))
a = int(input("Indique o valor de outro número: "))
print("Operações: 1=+, 2=-, 3=*, 4=/, 5=//, 6=%, 7=**")
op = int(input("Escolha uma das operações 1-7: "))

# Adição
if op == 1:
    op_adicao = a + b
    print("Adição ->", a, "+", b, "=", op_adicao)

# Subtração
elif op == 2:
    op_subtracao = a - b
    print("Subtração ->", a, "-", b, "=", op_subtracao)

# Multiplicação
elif op == 3:
    op_multiplicacao = a * b
    print("Multiplicação ->", a, "x", b, "=", op_multiplicacao)

# Divisão
elif op == 4:
    op_divisao = a / b
    print("Divisão ->", a, "/", b, "=", op_divisao)

# Divisão inteira
elif op == 5:
    op_divisao_int = a // b
    print("Divisão inteira ->", a, "//", b, "=", op_divisao_int)

# Módulo (resto da divisão)
elif op == 6:
    op_modulo = a % b
    print("Módulo ->", a, "%", b, "=", op_modulo)

# Exponenciação
elif op == 7:
    op_exponenciacao = a ** b
    print("Exponenciação ->", a, "**", b, "=", op_exponenciacao)
