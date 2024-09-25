# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

def calcular_media():
    soma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Digite um número (-1 para parar): "))
            
            if numero == -1:
                break
            
            soma += numero
            contador += 1
            
        except ValueError:
            print("Por favor, digite um número válido.")

    if contador > 0:
        media = soma / contador
        print(f"A média dos números digitados é: {media:.2f}")
    else:
        print("Nenhum número válido foi digitado.")

calcular_media()
