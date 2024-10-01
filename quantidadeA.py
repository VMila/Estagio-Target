def contaA(frase):
    numA = 0
    for i in frase:
        if(i == 'a' or i == 'A'):
            numA += 1

    return numA

frase = input("Digite uma frase: ")
quantA = contaA(frase)

print(f"A letra A aparece {quantA} vezes na frase")

