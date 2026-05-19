# Exercício 3- Nome decomposto verticalmente.
nome = input("Digite seu nome: ") # Pede para o usuário digitar o nome
qntdLetras = len(nome)  # Conta quantas letras o nome possui
# Percorre os números de 1 até a quantidade de letras do nome
for i in range(1, qntdLetras + 1, 1):
  print(nome[:i]) # Mostra o nome parcialmente até a posição atual