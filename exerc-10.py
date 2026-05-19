# Exercício 10- Sistema de Validação de Senha
print("Olá sejá bem vindo a tela de login! Primeiramente você deve colocar sua senha 👀")
senhaCorreta = 676767  # Define a senha correta do sistema

while True:  # Cria um laço infinito até a senha correta ser digitada

  senha = int((input("Digite aqui sua senha:  "))) # Recebe a senha digitada pelo usuário
  if  senha != senhaCorreta: # Verifica se a senha está incorreta
    print("A senha está incorreta, por favor tente novamente.")
    continue  # Faz o sistema repetir o laço novamente
  elif senha == senhaCorreta: 
  # Verifica se a senha está correta
    print("A senha está correta e foi autenticada com sucesso! Vamos te redirecionar para sua conta")
  break  # Encerra o laço após a senha correta