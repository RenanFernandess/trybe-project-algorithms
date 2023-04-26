<a name="readme-top"></a>
# :construction: README customizado em construção ! :construction:
<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto no qual você pode customizar e reutilizar todas as vezes que for executar o trybe-publisher.

Para deixá-lo com a sua cara, basta alterar o seguinte arquivo da sua máquina: ~/.student-repo-publisher/custom/_NEW_README.md

É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
# Algorithms

<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#construido-com">Construido Com</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando">Começando</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#ambiente-virtual">Ambiente virtual</a></li>
        <li><a href="#tests">Tests</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#contato">Contato</a></li>
    <li><a href="#agradecimentos">Agradecimentos</a></li>
  </ol>
</details>

## Sobre o Projeto
 
Neste projeto resolvi problemas e otimizar algoritmos desenvolvendo a minha capacidade de implementar soluções para os mais diversos problemas do dia a dia!

### Habilidades trabalhadas

* Lógica;
* Capacidade de interpretação de problemas;
* Capacidade de interpretação de um código legado;
* Capacidade de otimizar a resolução de problemas e;
* Resolver problemas/Otimizar algoritmos sob pressão.

### Construido Com

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![pytest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=ffdd54)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Começando

### Instalação

1. Clonar o repositorio

        git clone git@github.com:RenanFernandess/trybe-project-algorithms.git

2. Entrar na pasta project-job-insights

        cd ./trybe-project-algorithms

### Ambiente virtual

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **criar o ambiente virtual**

        python3 -m venv .venv

2. **ativar o ambiente virtual**

        source .venv/bin/activate

3. **instalar as dependências no ambiente virtual**

        python3 -m pip install -r dev-requirements.txt

> Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

### Tests

 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

    python3 -m pytest

  <details>
  <summary>Mais comandos</summary>
  
   O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

</details>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Uso

1. <details>
      <summary>study_schedule()</summary>
  
        study_schedule(permanence_period: list[(1, 2)], target_time: int)
      
      - Ex:
  
            # estudante             1       2       3       4       5       6
            permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
            
            study_schedule(permanence_period, 5) # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
            study_schedule(permanence_period, 4) # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
            study_schedule(permanence_period, 3) # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
            study_schedule(permanence_period, 2) # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
            study_schedule(permanence_period, 1) # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.
  
      - Retornos
        * Retorna a `quantidade de estudantes` presentes para uma entrada específica;
        * Retorna `None` se em permanence_period houver alguma entrada inválida;
        * Retorna `None` se target_time recebe um valor vazio;

    </details>

2. <details>
      <summary>is_palindrome_recursive()</summary>
      A função irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um booleano, True ou False.
  
          is_palindrome_recursive(word: str, low_index=0)

      Mas o que é um palíndromo?

      > Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, "ABCBA".
  
      - Ex:
          
              is_palindrome_recursive("ANA") # saída: True
              is_palindrome_recursive("SOCOS") # saída: True
              is_palindrome_recursive("COXINHA") # saída: False
              is_palindrome_recursive("AGUA") # saída: False
            
      - Retornos
        * Retorna `True` se a palavra passada por parâmetro for um palíndromo;
        * Retorna `False` se a palavra passada por parâmetro não for um palíndromo;
        * Retorna `False` se nenhuma palavra for passada por parâmetro.
        
    </details>
3. <details>
      <summary>is_anagram()</summary>
      
      O algoritmo que consiga comparar duas strings, ordená-las e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla() com a primeira string ordenada, a segunda string ordenada e um booleano, `True` ou `False` representando se são anagramas.
      
        is_anagram(first_string, second_string)
  
      O algoritmo considera letras maiúsculas e minúsculas como iguais durante a comparação das entradas, ou seja, ser case insensitive.

      Mas o que é um anagrama?

      > "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."
  
      - Ex:
          
              is_anagram("amor", "roma") # saída: ('amor', 'amor', True)
              # Explicação: Nesse caso a palavra 'amor' ordenada continua 'amor' e 'roma' ordenado vira 'amor, além disso a função é True, pois a palavra "roma" é um anagrama de "amor".
              
              is_anagram("pedra", "perda") # saída: ('adepr', 'adepr', True)
              # Explicação: Nesse caso o retorno também é True. Na palavra "pedra", trocamos o "d" de lugar com o "r" e formamos "perda", sendo assim um anagrama e temos as duas strings ordenadas.
                
              is_anagram("Amor", "Roma") # saída: ('amor', 'amor', True)
              # Explicação: Nesse caso o retorno da função é True, pois a palavra "Roma" é um anagrama de "Amor" independente da letra "R" e "A" serem maiúsculas.
              
              is_anagram("coxinha", "empada") # saída: ('achinox', 'aademp', False)
              # exemplo em que não existe um anagrama
              
            
      - Retornos
          * Retorna `True` se as palavras passadas por parâmetro forem anagramas;
          * Retorna `False` se as palavras passadas por parâmetro não forem anagramas;
          * Retorna `False` se alguma das palavras passadas por parâmetro for uma string vazia;
    </details>
4. <details>
      <summary>find_duplicate()</summary>
      Dada um array de números inteiros contendo n + 1 inteiros, chamado de nums, em que cada inteiro está no intervalo [1, n].
        
          find_duplicate(nums: int)
  
      - Ex:
          
              nums = [1, 3, 4, 2, 2]
              find_duplicate(nums) # saída: 2

              nums = [3, 1, 3, 4, 2]
              find_duplicate(nums) # saída: 3

              nums = [1, 1]
              find_duplicate(nums) # saída: 1

              nums = [1, 1, 2]
              find_duplicate(nums) # saída: 1

              nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
              find_duplicate(nums) # saída: 7
            
      - Retornos
          * Retorna o número repetivo se a função receber como parâmetro uma lista com números repetidos;
          * Retorna `False` se a função não receber nenhum parâmetro;
          * Retorna `False` se a função receber como parâmetro uma string;
          * Retorna `False` se a função receber como parâmetro uma lista sem números repetidos;
          * Retorna `False` se a função receber como parâmetro apenas um valor;
          * Retorna `False` se a função receber como parâmetro um número negativo;
        
   </details>
5. <details>
      <summary>is_palindrome_iterative()</summary>
      Resolva o mesmo problema apresentado no requisito 2 - Palíndromos, porém dessa vez utilizando a solução iterativa.
  
            is_palindrome_iterative(word: str)
  
      - Ex:
          
              is_palindrome_iterative("ANA") # saída: True
              is_palindrome_iterative("SOCOS") # saída: True
              is_palindrome_iterative("COXINHA") # saída: False
              is_palindrome_iterative("AGUA") # saída: False
            
      - Retornos
        * Retorna `True` se a palavra passada por parâmetro for um palíndromo;
        * Retorna `False` se a palavra passada por parâmetro não for um palíndromo;
        * Retorna `False` se nenhuma palavra for passada por parâmetro.
  
   </details>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Contato

* Renan Fernandes - [Linkedin](https://www.linkedin.com/in/orenanfernandes/) - renzinestuods@gmail.com

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Agradecimentos

* [Trybe](https://www.betrybe.com/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
