# Importacao das bibliotecas que serao utilizadas no projeto
import matplotlib.pyplot as plt
import numpy as np

# Valores possiveis para o eixo x 
# O primeiro valor do paretense representa o valor minimo do grafico
# O segundo o valor maximo
# O terceiro representa a definicao do grafico, sendo zero a maior definicao possivel
x = np.arange(-np.pi,np.pi, 0.0005)

# Parametros que diferenciam cada uma das funcoes: w, y e z
m1 = 1
m2 = 2
m3 = 3

# Valores que correspondem as funcoes que serao tracadas
w = np.cos(m1*x)
y = np.cos(m2*x)
z = np.cos(m3*x)
  
# Tracando o grafico de tres funcoes e colocando as marcacoes que vao diferenciar cada uma delas, incluindo o formato das linhas
plt.plot(x, w, 'k--', label='m = 1')
plt.plot(x, y, 'k:', label='m = 2')
plt.plot(x, z, 'k-.', label='m = 3')

# Nome do eixo x
plt.xlabel('x')
# Nome do eixo y
plt.ylabel('y')
  
# Colocando um titulo no gráfico que sera gerado
plt.title('Gráfico adimensional de y(t) = cos(m*t) para m = 1, 2 and 3')

# Criando uma legenda para o gráfico e posicionando ela no canto superior esquerdo
plt.legend(loc='upper left')
  
# Mostrando o grafico do resultado final
plt.show()