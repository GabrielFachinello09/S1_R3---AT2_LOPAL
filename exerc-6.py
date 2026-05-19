# Exercício 6- Identificação de Números Primos
# Para saber se um número é primo, o programa precisa testar se ele é divisível por algum número do meio (entre 2 e ele mesmo).
# Como todo número divide por 1 e por ele próprio, é importante usar o range(2, numero) porque ele faz exatamente isso: começa os testes no 2 (pulando o 1) e para um número antes do digitado (deixando o próprio número de fora).
# Se o laço for testar todos esses números intermediários e nenhum deles dividir o número com resto zero, ele será primo.


numero = int(input("Digite um número inteiro de  sua preferência: "))  # Recebe um número inteiro
# Verifica se o número é menor ou igual a 1
if numero <= 1:
  print("Esse número não é primo")
else:
# Percorre os números de 2 até o número digitado -1
  for i in range(2, numero):
     # Verifica se o número é divisível por algum valor
    if numero % i == 0:
      print(f"O número {numero}, que você  informou NÃO é primo")
      break # Interrompe o laço caso encontre um divisor
  else:
    print(f"O número {numero}, que você  informou É primo")     # Executa caso nenhum divisor seja encontrado