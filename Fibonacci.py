def fibonacci(n):
    a, b = 0, 1
    while(b < n):
        a, b = b, a + b
        if(b == n):
            return True
    return False

numero = int(input("Digite um numero para checarmos se esta na sequencia de Fibonacci: "))
is_fibonacci = fibonacci(numero)

if(is_fibonacci):
    print(f"O numero {numero} esta na sequência de Fibonacci")
else:
    print(f"O numero {numero} nao esta na sequência de Fibonacci")
