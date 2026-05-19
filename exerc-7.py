# Exercício 7- Fatoração de Números
numero = int(input("Forneça um número inteiro para o sistema realizar o fatorial deste número: ")) # Recebe um número inteiro
fatorial = 1 #Inicializa a variável do fatorial com 1
for i in range(numero, 1, -1): # Percorre os números do valor digitado até 2, em ordem decrescente
  fatorial = fatorial * i  # Multiplica o valor atual pelo próximo número

print(f"O fatorial de {numero} é: {fatorial}")