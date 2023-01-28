def Q19() :
    idade = int(input("Digite sua idade: "))

    if idade < 12 :
        print("Você é uma criança!")
    elif idade < 18 :
        print("Você é um adolescente!")
    elif idade < 30 :
        print("Você é um jovem!")
    elif idade < 60 :
        print("Você é um adulto!")
    else :
        print("Você é um idoso!")

def Q21() :
    n = float(input("Digite um número: "))

    if n % 2 == 0 :
        print(str(n) + " é par")
    else :
        print(str(n) + " é ímpar")
    
    if n < 0 :
        print(str(n) + " é negativo")
    elif(n > 0) :
        print(str(n) + " é positivo")
    else :
        print(str(n) + " é igual à 0")
    
    if n % 2 == 0 :
        print(str(n) + " é múltiplo de 2")

    if n % 3 == 0 :
        print(str(n) + " é múltiplo de 3")

    if n % 5 == 0 :
        print(str(n) + " é múltiplo de 5")

def Q23() :
    s = input("Digite seu sexo (m/f): ")
    peso = int(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em centímetros: ")) / 100
    imc = peso / (altura * altura)

    if s == "m" :
        if imc < 20.7 :
            print("Abaixo do peso")
        elif imc >= 20.7 and imc <= 26.4 :
            print("Peso ideal")
        elif imc >= 26.5 and imc <= 27.8 :
            print("Pouco acima do peso")
        elif imc >= 27.9 and imc <= 31.1 :
            print("Acima do peso")
        elif imc > 31.1 :
            print("Obeso")
    elif s == "f" :
        if imc < 19.1 :
            print("Abaixo do peso")
        elif imc >= 19.1 and imc <= 25.8 :
            print("Peso ideal")
        elif imc >= 25.9 and imc <= 27.3 :
            print("Pouco acima do peso")
        elif imc >= 27.4 and imc <= 32.3 :
            print("Acima do peso")
        elif imc > 32.3 :
            print("Obesa")

def Q25() :
    n = 50

    print("Digite s para sim e n para não!")
    r1 = input("Você curtiu o link? ") == "s"
    r2 = input("Você segue o perfil da empresa no facebook? ") == "s"
    r3 = input("Você está no grupo do whatsapp? ") == "s"
    r4 = input("Você segue o perfil da empresa no twitter? ") == "s"
    r5 = input("Você retweetou o link da promoção? ") == "s"

    if r1 : n *= 2
    if r2 : n *= 3
    if r3 : n *= 4
    if r4 : n *= 2
    if r5 : n *= 3

    print("\nParabéns seu prêmio é de R$", n)