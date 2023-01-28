def IMC() :
    altura = float
    peso = float
    imc = float

    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    imc = peso / (altura * altura)

    print("Seu IMC é: " + str(imc))

