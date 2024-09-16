# Passo 1: Solicitar a entrada dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar(+, -, *, /): ")

# Passo 2: Realizar a operação
if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(abs(numero1 - numero2))
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    print(numero1 / numero2)
else:
    print("Operação Inválida")
    #use a ia para entender como funciona e assim melhore.