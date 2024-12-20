#Calculadora Simples
# Receber um numero 
# Receber um operador
# Receber um outro numero
# Mostrar o Resultado

import operator

dict_operadores = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

print("Digite um numero")
numero1 = int(input())

print("Digite um operador")
operador = input()

print("Digite um segundo numero")
numero2 = int(input())

print(dict_operadores[operador](numero1, numero2))
