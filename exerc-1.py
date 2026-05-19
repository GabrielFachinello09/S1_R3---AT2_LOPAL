## Exercício 1- Número Ímpar e Par 1,2:

for numero in range(0,101): # Percorre os números de 0 até 100
  if numero % 2 == 0:   # Verifica se o número é divisível por 2
    print(f"{numero}: Este número é par") # Exibe que o número é par
  else:
    print(f"{numero}:Este número é ímpar") # Exibe que o número é ímpar