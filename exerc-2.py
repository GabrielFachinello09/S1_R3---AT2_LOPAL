# Exercício 2- Identificação de Maior e Menor Número de Lista
num1 = int(input("Digita o primeiro número: "))
num2 = int(input("Digita o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
lista = [num1, num2, num3]  # Cria uma lista com os números digitados
lista.sort() # Organiza a lista em ordem crescente
primeiroNum = lista[0] #Pega o maior número da lista
ultimoNum = lista[2] #Pega o menor núméro da lista

# Exibe o menor e o maior número
print(f"O menor número desta sequência fornecida é {primeiroNum}, e o maior número é {ultimoNum}")