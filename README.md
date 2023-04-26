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

            target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
  
      - Retornos
        * Retorna a `quantidade de estudantes` presentes para uma entrada específica;
        * Retorna `None` se em permanence_period houver alguma entrada inválida;
        * Retorna `None` se target_time recebe um valor vazio;

</details>

2. <details>
      <summary>is_palindrome_recursive()</summary>
          is_palindrome_recursive(word, low_index)
        
    </details>
3. <details>
      <summary>is_anagram()</summary>
          is_anagram(first_string, second_string)
        
    </details>
4. <details>
      <summary>find_duplicate()</summary>
          find_duplicate(nums)
        
   </details>
5. <details>
      <summary>is_palindrome_iterative()</summary>
          is_palindrome_iterative(word)
        
   </details>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Contato

* Renan Fernandes - [Linkedin](https://www.linkedin.com/in/orenanfernandes/) - renzinestuods@gmail.com

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Agradecimentos

* [Trybe](https://www.betrybe.com/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
