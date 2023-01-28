import math

def Atividades() :
    massa = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc = massa / (altura * altura)
    print('Seu IMC é: ', imc)

def CalculoDeNotas() :
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(media)

def MetrosParaCent() :
    metros = float(input('Digite a distância em metros: '))
    print("A distância em centímetros é:", metros * 100)

def AreaTriangulo() :
    base = float(input('Digite o tamanho da base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))
    area = base * altura / 2

    print('A área do triângulo é:', area)

def AreaQuadrado() :
    lado = float(input('Digite o tamanho do lado do quadrado: '))
    area = lado ** 2

    print('A área do quadrado é:', area)

def AreaRetangulo() :
    lado1 = float(input('Digite o tamanho de um lado do retângulo: '))
    lado2 = float(input('Digite o tamanho do outro lado do retângulo: '))
    area = lado1 * lado2

    print('A área do retângulo é:', area)

def AreaTrapezio() :
    bMaior = float(input('Digite o tamanho da base maior do trapézio: '))
    bMenor = float(input('Digite o tamanho da base menor do trapézio: '))
    altura = float(input('Digite o tamanho da altura do trapézio: '))
    area = (bMaior + bMenor) * altura / 2

    print('A área do trapézio é:', area)

def AreaLosango() :
    diagonal1 = float(input('Digite o tamanho de uma diagonal do losango: '))
    diagonal2 = float(input('Digite o tamanho da outra diagonal do losango: '))
    area = diagonal1 * diagonal2 / 2

    print('A área do losango é:', area)

def AreaCirculo() :
    raio = float(input('Digite o tamanho do raio do círculo: '))
    area = (raio ** 2) * math.pi

    print('A área do círculo é:', area)

def Sequencia() :
                                     # O código é executado em ordem de cima para baixo
    a = 3                            # A primeira linha é executada
    b = 4                            # Depois disso a segunda linha é executada
    c = 0.0                          # A terceira linha é executada
    c = ((a ** 2) + (b ** 2)) ** 0.5 # A quarta linha é executada
    print(c)                         # A quinta linha é executada
                                     # Se não possuir mais nada abaixo, então o programa finaliza

def Selecao() :
                                               # Permite selecionar certas partes do código a serem executadas
    a = 1                                      # Especifica uma variável inteira

    if a > 0 :                                 # Verifica se a variável é maior ou igual a 0
        print(str(a) + " é maior do que 0")    # Se for verdadeiro, então executa uma parte do código
    elif a < 0:
        print(str(a) + " é menor do que 0")    # Se for falsa, então executa uma outra parte do código
    else :
        print(str(a) + " é igual à 0")         # Se não for nenhum dos casos acima, parte restante do código

def Iteracao() :
                   # Permite que certas partes do código sejam repetidas uma certa quantia de vezes
    a = 0          # Inicia uma variável com valor 0

    while a < 10 : # Enquanto 'a' for menor do que 0, essa parte do código se repete
        print(a)   # Escreve 'a'
        a += 1     # Adiciona 1 em 'a'