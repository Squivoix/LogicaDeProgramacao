def fatorial(valor) :
    
    num = 0
    
    while num < valor :
        if valor == 1 or valor == 0 :
            return 1
        elif valor < 0 :
            return -1
        else :
            return valor * fatorial(valor - 1)

        num += 1

cont = int(input("Digite um número: "))
res = fatorial(cont)

print(res)
