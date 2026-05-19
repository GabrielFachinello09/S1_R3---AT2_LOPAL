# #Exercício 4- Sequência Fibonacci
# Primeiramente o sistema vai solicitar ao usuário que digite um número. O input() recebe esse valor como texto (string), o int() transforma esse texto em um número inteiro, e o resultado é guardado na variável n.

# As váriaveis: penultimo = 1 ultimo = 1 Inicializam os dois primeiros números da sequência de Fibonacci. Por definição, a sequência começa com 1 e 1.

# if n <= 0:
#   print("Por favor, digite um número maior que zero.")
# A primeira condicional vai verificar se o usuário digitou um número menor ou igual a zero. Se sim, exibe uma mensagem falando que não faz sentido pedir "zero" ou "menos três" termos da sequência, por causa dos números iniciais que já foram definidos.

# elif n == 1:
#   print(penultimo)
# Caso o usuário tenha pedido exatamente 1 termo, o programa apenas imprime o primeiro termo da sequência, que é 1 (guardado em penultimo no começo do código).

# elif n == 2:
#   print(f"{penultimo}, {ultimo}")
# Se o usuário pediu exatamente 2 termos, o programa imprime os dois primeiros números separados por uma vírgula (1, 1).

# Laço de Repetição (Para 3 ou mais termos):

# contador = 3
# Cria uma variável para controlar as repetições do laço. Como os dois primeiros termos já estão definidos, o cálculo real da sequência começa a partir do terceiro termo.

# while contador <= n:
# Inicia um laço de repetição (while significa "enquanto"). O código dentro dele vai rodar repetidamente enquanto o valor de contador for menor ou igual ao número n que o usuário digitou.

# atual = penultimo + ultimo
# Calcula o termo atual da sequência. Na lógica de Fibonacci, o próximo número é sempre a soma dos dois anteriores.

# print(f"{atual}", end="")
# Imprime o número atual na tela. O argumento end="" serve para que o Python não pule uma linha automaticamente após imprimir o número.

# penultimo = ultimo
# Atualiza as variáveis para a próxima rodada. O que era o ultimo número agora passa a ser o penultimo.

# ultimo = atual
# O número que acabou de ser calculado (atual) agora passa a ser o ultimo. Com isso, a fila "anda" para o próximo cálculo.

# contador += 1
# Soma 1 ao valor do contador (o mesmo que contador = contador + 1). Isso garante que o laço avance e não fique rodando para sempre (loop infinito).

# print()
# Imprime uma linha em branco. Como está dentro do while, isso faz com que, a cada repetição, o programa pule para a próxima linha antes de calcular o próximo número. (coloquei apenas os valores ficarem mais claro)

n = int(input("Digite quantos termos da série de Fibonacci você deseja: "))
penultimo = 1
ultimo = 1

if n <= 0:
  print("Por favor, digite um número maior que zero.")
elif n ==1:
  print(penultimo)
elif n == 2:
  print(f"{penultimo}, {ultimo}")

contador = 3
while contador <= n:
      atual = penultimo + ultimo
      print(f"{atual}", end="")

      penultimo = ultimo
      ultimo = atual
      contador += 1
      print()

