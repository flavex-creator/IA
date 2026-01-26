'''Exemplo da elaboração de um gráfico, utilizando funções do módulo pyplot da
biblioteca matplotlib'''

# Importação do módulo pyplot da biblioteca matplotlib
import matplotlib.pyplot

# Listas de valores a ser apresentados no gráfico
matplotlib.pyplot.plot(
    ["Jan.", "Fev.", "Mar.", "Abr.", "Maío", "Jun.", "Jul.", "Ago.",
     "Set.", "Out.", "Nov.", "Dez."],
    [9.03, 9.78, 12.37, 13.99, 16.78,
     20.39, 22.54, 22.92, 20.48, 16.84, 12.28, 9.75],
    '-o',
    color="purple",
    linewidth=3
)

# Apresenta o titulo do gráfico
matplotlib.pyplot.title(
    'Temperatura Média 1991-2019 (Portugal Continental - Fonte IPMA)'
)

# Apresenta o rótulo do eixo do y
matplotlib.pyplot.ylabel('Temperatura (ºC)')

# Apresenta o rótulo do eixo do x
matplotlib.pyplot.xlabel('Mês')

# Apresenta a grelha do gráfico
matplotlib.pyplot.grid()

# Apresenta o gráfico numa janela
matplotlib.pyplot.show()
