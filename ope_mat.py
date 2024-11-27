#Solicitar como entrada dois numeros e realizar uma ioeração matematica entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: ")) 

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        print("Erro: Divisão por zero")
    else:
        resultado = num1 / num2
else:
    print("Operação inválida")
    exit()

print("Resultado:", resultado)
