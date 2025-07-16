# calculadora.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Calculadora em Python")
print("Selecione a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

op = input("Digite o número da operação: ")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == '1':
    print("Resultado:", somar(a, b))
elif op == '2':
    print("Resultado:", subtrair(a, b))
elif op == '3':
    print("Resultado:", multiplicar(a, b))
elif op == '4':
    print("Resultado:", dividir(a, b))
else:
    print("Operação inválida")
