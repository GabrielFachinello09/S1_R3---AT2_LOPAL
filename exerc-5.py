# Exercício 5- Questionário Pessoal
print("Boa tarde, começaremos agora nosso questionário de informações pessoais necessárias para cadastrar você em nossa empresa! 🤖")

nome = str(input("Digite seu primeiro nome: "))
qntdLetras = len(nome)
if qntdLetras > 3:
  print("Seu nome tem mais do que 3 caracteres")
elif qntdLetras == 3:
  print("Seu nome tem exatamente 3 caracteres")
else:
  print("Seu nome tem menos do que 3 caracteres")

print("="*100)


while True:
  idade = int(input("Digite sua idade: "))

  if idade > 151 or idade < 0:
    print("As informações devem estar erradas, por favor tente novamente!")
    continue

  if idade > 3 and idade <= 12:
    print(f"Com apenas {idade} anos, você ainda é uma criança!")
  elif idade > 10 and idade <= 19:
    print(f"Com {idade} anos, você já está na fase da adolescência! ")
  elif idade > 20 and idade <= 39:
    print(f"Sua idade é de {idade} anos, sendo assim, você se enquadra como jovem adulto.")
  elif idade > 40 and idade <= 59:
    print(f"Você está com {idade} anos, logo, é considerado uma pessoa de meia-idade")
  else:
    print(f"Sua idade é de {idade} anos, sendo assim, você já faz parte da terceira idade.")

  break


print("="*100)

while True:
  salarioMensal = float(input("Nos informe quanto você recebe por mês de sálario. Observação: Deixe o valor com os centavos- "))

  if salarioMensal == 1621.00:
    print("Você recebe o equivalente a um sálario mínimo.")
  elif salarioMensal > 1621.00:
    print("Você recebe mais que um sálario mínimo")

  elif salarioMensal < 0 or salarioMensal < 1621.00:
    print("O valor que você informou deve estar errado, visto que o salário mínimo do Brasil é R$ 1.621,00, por favor, digite novamente!")
    resp = input("Você trabalha na informalidade? ")

    if resp.strip().lower() == "sim":
      print("Tome cuidado! Sem um registro formal você se expõe à falta de proteção social, como seguro-desemprego, auxílio-doença, licença-maternidade e contagem de tempo para aposentadoria.")
    elif resp.strip().lower() == "não": #A função deixa a string minúscula, para que não haja incoerência mesmo com a pessoa respondendo "NÃO".
      print("Caso sua jornada seja comum (44 horas semanais), converse com o setor de Recursos Humanos da sua empresa ou com o seu sindicato para verificar se há algum erro no seu pagamento.")
  break


print("="*100)

while True:
    sexo = str(input("Qual é o seu gênero, o sistema aceita apenas respostas como 'F' e 'M': ")).strip().lower()
    if sexo in ['f', 'm']: #O sistema continua a perguntar até que as informações estejam corretas.
      print("A resposta está adequada as orientações.") 
      break #Quando a resposta for F, f, M, m. Que é o adequado, o laço vai parar de ser correspondido.
    else:
      print("A  informação deve estar errada, as únicas opções válidas são: \n'F'= feminino \n'M'= masculino \nPor favor informe novamente qual é o seu sexo.")

print("="*100)

while True:
    estadoCivil = str(input("Qual é o estado civil, o sistema aceita apenas respostas como 'c', 's', 'v', 'd': ")).strip().lower()
    if estadoCivil in ['c', 's', 'v', 'd']:
      print("Estado Civil registrado com sucesso.")
      break
    else:
      print("A  informação deve estar errada. Caso você não tenha entendido as iniciais tem os seguintes significados:\n 'C' - Casado(a)\n 'S' - Solteiro\n 'V'- Víuvo (a)\n 'D'- Divorciado(a)\n Por favor leia novamente a pergunte e informe seu estado civil seguindo as orientações.")

print("="*100)

print("Agora você deve verificar as respostas que você nos forneceu! 🤖")

print(f"As informaçções coletadas foram as seguintes:\n -Seu nome é {nome}\n -Você tem {idade} anos\n -Você recebe {salarioMensal} reais por mês\n -Você é do sexo: {sexo}\n -Seu estado civil é: {estadoCivil}")
verificacao = input("As informações estão corretas? ").strip().lower()
if verificacao == 'sim':
  print("Verificação feita com êxito, o questionário foi concluido 🤖")
elif verificacao == 'não':
  print("Por favor, reinicie o formulário e preencha novamente com as informações certas!")


print("→_→"*100)