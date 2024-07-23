palavra = input("Digite uma palavra: ").lower().strip().replace(' ', '')

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se é um palíndromo
if palavra == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")