# Exercício 8- Identificação e Fatiamento de valores de Lista
from pprint import pprint  # Importa a função pprint para exibir os números formatados

l = [5, 7, 2, 9, 4, 1, 3]  # Cria uma lista com números inteiros
tamanhoLista = len(l)  # Conta a quantidade de elementos da lista
print(f"A quantidade de caracteres da lista de números é igual a {tamanhoLista}")
maiorNum = max(l)  # Identifica o maior número da lista
print(f"O maior número dentre todos os outros é o {maiorNum}")
menorNum = min(l)  # Identifica o menor número da lista
print(f"O menor número dentre todos os outros é o {menorNum}")

print("-"*100)

print(f"A sequência decrescente dos números fornecidos pela lista é igual a:")
for i in range (maiorNum, menorNum -1, -1): # Percorre os números do maior até o menor em ordem decrescente
  pprint(i)

print("-"*100)

print(f"A sequência crescente dos números fornecidos pela lista é igual a:")
for i in range (menorNum, maiorNum + 1, 1): # Percorre os números do menor até o maior em ordem crescente
  pprint(i)
