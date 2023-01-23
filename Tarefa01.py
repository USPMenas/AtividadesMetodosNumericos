# Importacao das bibliotecas que serao utilizadas no projeto
import matplotlib.pyplot as plt
import numpy as np

#QUESTAO 1
def quest1():
    # Valores possiveis para o eixo x 
    # O primeiro valor do paretense representa o valor minimo do grafico
    # O segundo o valor maximo
    # O terceiro representa a definicao do grafico, sendo zero a maior definicao possivel
    x = np.arange(-np.pi, np.pi, 0.0005)

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
    plt.title('Gráfico adimensional de y(t) = cos(m*t) para m = 1, 2 e 3')

    # Criando uma legenda para o gráfico e posicionando ela no canto superior esquerdo
    plt.legend(loc='upper left')
    
    # Mostrando o grafico do resultado final
    plt.show()

#QUESTAO 2.1
def quest2_1():
    # Definindo o número de passos minimo
    n = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    h = np.zeros(len(n))
    erros = np.zeros(len(n))
    ordemP = np.zeros(len(n))
    
    # Definindo o intervalo a ser utilizado, sendo o modelo do intervalo igual a [a,b]
    a = 0
    b = 1/2
    
    # Definindo o tamanho do passo
    for i in range(len(n)):
        h[i] = (b-a)/n[i]
        
    # Derivada associada a solução exata, solução exata escolhida: y(t) = sin(2π*t)*e^(−0.2)*t
    
    t_inicial = 0 # Valor inicial do passo no eixo das abcissas
    y_inicial =  # Valor de y'(t0,y0)
    y_numerico = y_inicial # Valor inicial do y_numerico na extremidade inferior [a, ...]
    
    # Aplicação do método de Euler para todos os valores de n 
    for i in range(len(n)):
    # O laço externo serve para alternar entre os diferentes valores de n propostos
    
        # Laço interno para calcular o valor do y númerico para cada valor de n
        for j in range(n[i]-1):
            t_inicial += h[i]
            y_linha = 2*np.pi*np.cos(2*np.pi*t_inicial)*np.exp(-0.2*t_inicial)-0.2*(np.sin(2*np.pi*t_inicial)*np.exp(-0.2*t_inicial))
            y_numerico += h[i] * y_linha
        
        y_real = np.sin(2*np.pi*t_inicial)*np.exp(-0.2*t_inicial)
        erros[i] = np.absolute(y_real - y_numerico)
        #print(f'{erros[i]:.4e}')
        
        # Reiniciando os valores para um novo valor de tamanho de passo
        t_inicial = 0
        y_numerico = y_inicial
        
    # Encontrando  a constante r
    r = h[0] / h[1]
        
    for i in range(len(n)-1):
        ordemP[i+1] = np.log2(erros[i] / erros[i+1]) / np.log2(r)
        
    print(f"n \t &&& \t h_n \t\t &&& \t |e(T,h_n)| \t &&& \t ordem P")
    for i in range(len(n)):
        
        if i == 0:
            print(f"{n[i]} \t &&& \t {h[i]:.4e} \t &&& \t {erros[i]:.4e} \t &&& \t ------")
        else:
            print(f"{n[i]} \t &&& \t {h[i]:.4e} \t &&& \t {erros[i]:.4e} \t &&& \t {ordemP[i]:.5}")
        
    
                                        

#QUESTAO 2.2


#QUESTAO 2.3


#Function main utilizada para unir o fluxo de dados da resolução das questões para o usuário.

def main():
    #quest1()
    quest2_1()
    
main()