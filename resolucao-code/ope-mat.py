n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Define as operações disponíveis
operacoes = {
    1: ("soma", n1 + n2),
    2: ("subtração", n1 - n2),
    3: ("multiplicação", n1 * n2),
    4: ("divisão", n1 / n2) if n2 != 0 else "Erro: divisão por zero não é permitida."
}

# Recebe a escolha do usuário
opcao = int(input("Escolha a operação (1 a 4): "))

# Exibe o resultado da operação selecionada
if opcao in operacoes:
    nome_operacao, resultado = operacoes[opcao]
    print(f"A {nome_operacao} é:", resultado)
else:
    print("Opção inválida. Escolha um número de 1 a 4.")

# Fim do programa
print("Obrigado por usar nosso programa!")
