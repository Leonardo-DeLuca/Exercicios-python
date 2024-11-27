#Solicitar uma string e um numero inteiro como entrada. Depois retornar a string repetindo o número de vezes retornado.

string = input("Digite a string: ") 
numero = int(input("Digite o número de repetições: ")) 

resultado = string * numero 
for i in range(numero):
    print(string)
