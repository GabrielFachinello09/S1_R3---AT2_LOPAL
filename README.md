#  Exercícios Práticos: Lógica de Programação com Python

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status Concluído">
</p>

<p align="justify">
  Este repositório contém uma coleção de exercícios práticos desenvolvidos para o aprendizado e consolidação de conceitos fundamentais de lógica de programação utilizando a linguagem Python. Os scripts abordam desde estruturas condicionais simples até laços de repetição e manipulação de estruturas de dados.
</p>

---

## 📂 Detalhes dos Exercícios

### 📋 Exercício 1: Identificação de Números Pares e Ímpares

<p align="center">
  <img width="500" alt="Código Exercício 1" src="https://github.com/user-attachments/assets/ca77bddb-0b79-4933-a985-4ec18c57c668" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo percorrer todos os números de 0 até 100 e identificar se cada valor é par ou ímpar. Para isso, foi utilizada a estrutura de repetição <code>for</code> junto da função <code>range(0, 101)</code>, responsável por gerar a sequência numérica. Durante cada repetição, o programa aplica uma verificação utilizando o operador módulo <code>%</code>, que retorna o resto da divisão do número por 2. Quando o resultado da operação é igual a 0, o número é classificado como par, caso contrário, é considerado ímpar. Em seguida, o programa exibe uma mensagem formatada informando o número analisado e sua respectiva classificação.
  </p>
</blockquote>

### 📋 Exercício 2: Identificação de Maior e Menor da Lista (Exerc-2.py)

<p align="center">
  <img width="500" alt="Código Exercício 2" src="https://github.com/user-attachments/assets/47349ede-af7b-4a3b-9422-6053c1dbb24d" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Explicação Técnica:</strong> O programa recebe três números inteiros do usuário e os armazena em uma lista. Em seguida, utiliza o método <code>.sort()</code> para ordenar os elementos em ordem crescente. Com a lista ordenada, o sistema identifica o menor número no índice zero <code>[0]</code> e o maior número no último índice <code>[2]</code>, exibindo os resultados formatados na tela. <code>[2]</code>.
  </p>
</blockquote>

### 📋 Exercício 3: Nome Decomposto Verticalmente

<p align="center">
  <img width="500" alt="Código Exercício 3" src="https://github.com/user-attachments/assets/a2426898-9144-4334-972d-44d9f3805142" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> Este código solicita o nome do usuário e calcula a quantidade de caracteres usando a função <code>len()</code>. Através de uma estrutura de repetição <code>for</code> combinada com o fatiamento de strings (<em>slicing</em>), o programa exibe o nome de forma progressiva e vertical, adicionando uma letra a mais a cada linha até completar o nome.
  </p>
</blockquote>

### 📋 Exercício 4: Sequência de Fibonacci

<p align="center">
  <img width="500" alt="Código Exercício 4" src="https://github.com/user-attachments/assets/5991839c-fd06-4c16-a6b5-91d576293c35" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo gerar e exibir os termos da sequência de Fibonacci de acordo com a quantidade informada pelo usuário. Inicialmente, o programa utiliza a função <code>input()</code> para solicitar ao usuário o número de termos desejados e a função <code>int()</code> para converter o valor digitado em um número inteiro. Em seguida, são definidas as variáveis <code>penultimo</code> e <code>ultimo</code>, ambas iniciadas com o valor 1, representando os primeiros termos da sequência de Fibonacci. O código também utiliza estruturas condicionais (<code>if</code>, <code>elif</code>) para tratar situações específicas, como valores menores ou iguais a zero e casos em que o usuário deseja apenas um ou dois termos da sequência que nesse caso já são definidas como 1,1. Após essas verificações, é utilizada a estrutura de repetição <code>while</code>, responsável por calcular os próximos números da sequência até atingir a quantidade solicitada. Durante cada repetição, o programa soma os dois últimos valores para gerar o próximo termo da sequência, updating as variáveis e exibindo os resultados na tela. OBSERVAÇÃO: Explicação mais detalhada no arquivo (Exerc-4.py).
  </p>
</blockquote>

### 📋 Exercício 5: Questionário Pessoal e Validação de Dados

<p align="center">
  <img width="500" alt="Código Exercício 5" src="https://github.com/user-attachments/assets/efd3d6b3-dc80-49ca-8677-47f8cff4e9dc" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código realiza um questionário interativo para cadastro empresarial. Inicialmente, solicita o primeiro nome com <code>input()</code> e mede seu comprimento com <code>len()</code> para validar a quantidade de caracteres. Em seguida, utiliza laços de repetição <code>while</code> para garantir a consistência das entradas. O sistema valida a idade e a classifica em faixas etárias como infância, adolescência ou idade adulta. Na etapa salarial, compara o valor ao salário mínimo nacional, emitindo alertas sobre informalidade. Por fim, o programa valida o sexo e o estado civil aceitando apenas opções predefinidas, exibindo todas as informações coletadas ao término para conferência.
  </p>
</blockquote>

### 📋 Exercício 6: Identificação de Números Primos

<p align="center">
  <img width="500" alt="Código Exercício 6" src="https://github.com/user-attachments/assets/20076c8b-5bd9-4d04-a9de-0601b5c9ba3f" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo verificar se um número inteiro fornecido pelo usuário é primo. Inicialmente, o programa descarta valores menores ou iguais a 1, classificando-os direto como não primos. Para os demais valores, utiliza-se a estrutura de repetição <code>for</code> junto da função <code>range(2, numero)</code>, responsável por testar a divisibilidade por qualquer número intermediário. Durante cada iteração, o programa aplica uma verificação com o operador módulo <code>%</code> e, caso encontre um resto igual a 0, utiliza o comando <code>break</code> para interromper o laço imediatamente. Se a repetição for concluída sem interrupções, a estrutura condicional <code>else</code> associada ao bloco do laço classifica o número analisado como primo.
  </p>
</blockquote>

### 📋 Exercício 7: Fatoração de Números

<p align="center">
  <img width="500" alt="Código Exercício 7" src="https://github.com/user-attachments/assets/4413c71e-4fd2-4cd8-99af-5ce827e240c3" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo calcular o fatorial de um número inteiro fornecido pelo usuário. Inicialmente, o programa utiliza a função <code>input()</code> para capturar o valor e a função <code>int()</code> para convertê-lo em tipo inteiro. Uma variável acumuladora chamada <code>fatorial</code> é definida com o valor inicial 1. Em seguida, utiliza-se a estrutura de repetição <code>for</code> junto da função <code>range(numero, 1, -1)</code>, responsável por percorrer a sequência numérica em ordem decrescente a partir do número informado até o valor 2. Durante cada repetição, o programa multiplica o valor acumulado pelo número atual da iteração. Por fim, o programa exibe uma mensagem formatada informando o número analisado e o resultado do seu fatorial.
  </p>
</blockquote>

### 📋 Exercício 8: Análise, Ordenação e Fatiamento de Listas

<p align="center">
  <img width="500" alt="Código Exercício 8" src="https://github.com/user-attachments/assets/ca04c34b-103c-4b5a-b3d5-020771f0596e" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo realizar um diagnóstico completo sobre uma lista predefinida de números inteiros. Inicialmente, o programa utiliza as funções <code>len()</code>, <code>max()</code> e <code>min()</code> para contar os elementos da lista e identificar o maior e o menor valor presente, exibindo esses metadados na tela. Em seguida, o sistema implementa duas estruturas de repetição <code>for</code> associadas à função <code>range()</code>. A primeira percorre o intervalo em ordem decrescente (do maior ao menor número), enquanto a segunda faz a varredura em ordem crescent (do menor ao maior). Durante cada iteração dos laços, utiliza-se a função <code>pprint()</code> para exibir os números sequenciais de forma formatada e limpa no console.
  </p>
</blockquote>

### 📋 Exercício 9: Dicionário de Lanchonete

<p align="center">
  <img width="500" alt="Código Exercício 9" src="https://github.com/user-attachments/assets/3f10d937-5afb-4112-bde0-bdd73ba9703f" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo estruturar o cardápio de uma lanchonete associando os produtos aos seus respectivos preços reais. Para isso, foi utilizada a estrutura de dados de dicionário em Python, mapeando as informações através de pares de chave e valor, onde as chaves representam os nomes dos alimentos em formato de texto e os valores armazenam os preços em formato numérico decimal. Ao final, o programa utiliza a função <code>print()</code> para exibir toda a estrutura organizada do dicionário no console.
  </p>
</blockquote>

### 📋 Exercício 10: Sistema de Validação de Senha

<p align="center">
  <img width="500" alt="Código Exercício 10" src="https://github.com/user-attachments/assets/67a5598e-2823-4199-a0a6-288cb6917ad0" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo simular uma tela de login que valida o acesso de um utilizador através de uma palavra-passe. Inicialmente, o sistema define o segredo numérico correto e inicia uma estrutura de repetição <code>while True</code> para criar um laço de captura contínuo. Durante cada ciclo, o programa utiliza as funções <code>input()</code> e <code>int()</code> para recolher e converter a tentativa digitada. Através de verificações condicionais (<code>if</code>, <code>elif</code>), o sistema avalia a entrada: se o valor for incorreto, o comando <code>continue</code> é acionado para reiniciar o laço imediatamente; caso a palavra-passe seja correspondente, uma mensagem de sucesso é exibida e o comando <code>break</code> encerra o programa.
  </p>
</blockquote>

### 📋 Exercício 11: Sistema de Tabuada Automatizada

<p align="center">
  <img width="500" alt="Código Exercício 11" src="https://github.com/user-attachments/assets/14a3ae91-c310-4475-82c3-d44e89bf84d9" />
</p>

<blockquote>
  <p align="justify">
    <strong>💡 Abordagem Prática:</strong> O código tem como objetivo gerar e exibir a tabuada de multiplicação de um número inteiro fornecido pelo utilizador. Inicialmente, o programa utiliza as funções <code>input()</code> e <code>int()</code> para recolher e converter o valor base do console. Em seguida, é utilizada a estrutura de repetição <code>for</code> associada à função <code>range(1, 11, 1)</code>, responsável por ditar a sequência dos multiplicadores de 1 até 10. Durante cada iteração, o sistema calcula o produto entre o número informado e a variável de controlo do laço. Por fim, o programa utiliza uma sintaxe de f-string para apresentar os resultados das operações matemáticas formatados linha a linha.
  </p>
</blockquote>

---

## 🛠️ Caixa de Ferramentas: Funções & Comandos

<table align="center" width="100%">
  <thead>
    <tr style="background-color: #1f2328; border-bottom: 2px solid #30363d;">
      <th align="left" style="padding: 10px;">🔧 Função / Comando</th>
      <th align="left" style="padding: 10px;">📝 Descrição Breve</th>
      <th align="left" style="padding: 10px;">💻 Exemplo de Aplicação</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>print()</code></td>
      <td>Exibe mensagens ou dados na tela de saída.</td>
      <td><code>print(f"O número é {num}")</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>input()</code></td>
      <td>Recebe dados enviados pelo usuário via teclado (retorna string).</td>
      <td><code>nome = input("Digite seu nome")</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>range()</code></td>
      <td>Gera uma sequência de números com base em início, fim e passo.</td>
      <td><code>range(0, 101)</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>len()</code></td>
      <td>Retorna a quantidade de elementos de um objeto (lista, string, etc.).</td>
      <td><code>qntd = len(lista)</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>int()</code> / <code>float()</code></td>
      <td>Converte um valor ou string para o tipo inteiro ou decimal.</td>
      <td><code>idade = int(input())</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>.sort()</code></td>
      <td>Ordena os elementos de uma lista em ordem crescente.</td>
      <td><code>lista.sort()</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>max()</code> / <code>min()</code></td>
      <td>Identifica o maior ou o menor valor dentro de uma coleção.</td>
      <td><code>maior = max(lista)</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>.strip()</code> / <code>.lower()</code></td>
      <td>Remove espaços extras e converte strings para letras minúsculas.</td>
      <td><code>resp.strip().lower()</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #21262d;">
      <td style="padding: 10px;"><code>break</code> / <code>continue</code></td>
      <td>Interrompe o laço de repetição ou avança para a próxima iteração.</td>
      <td>Se a senha estiver correta, executa <code>break</code>.</td>
    </tr>
  </tbody>
</table>

---
<p align="center">Desenvolvido com 🐍 por <strong>Gabriel Fachinello</strong></p>





