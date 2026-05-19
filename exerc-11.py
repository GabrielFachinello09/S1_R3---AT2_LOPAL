# Exercício 11- Sistema que Informa a Tabuada de um Número
numero = int(input(("Peça um número entre 1 a 10: "))) # Recebe um número inteiro do usuário
for i in range(1,11,1): 
# Percorre os números de 1 até 10
  multiplicacao = numero * i  #Realiza a multiplicação do número pelo valor atual
  print(f"{numero} X {i} = {multiplicacao}") #
  # Exibe o resultado da tabuada
