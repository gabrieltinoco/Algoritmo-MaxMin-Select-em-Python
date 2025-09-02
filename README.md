# Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python

**Trabalho Individual 2 da disciplina de Fundamentos de Projetos e Análise de Algoritmos.**

## Objetivo

Desenvolver um programa em Python que implemente o algoritmo de seleção simultânea do maior e do menor elementos (MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista.

## O que é o Algoritmo MaxMin Select?

O algoritmo de seleção simultânea (MaxMin Select) pode ser implementado de forma recursiva, utilizando a técnica de divisão e conquista. O problema é dividido em subproblemas menores que são resolvidos recursivamente, e seus resultados são combinados para encontrar o maior e o menor elementos com eficiência. Esse método reduz o número de comparações necessárias em comparação com uma abordagem ingênua. 

## Explicação do Algoritmo

### Implementação Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)

```python
def max_min_select(lista):
    tamanho_lista = len(lista)

    if tamanho_lista == 0:
        return (None, None)

    if tamanho_lista == 1:
        return (lista[0], lista[0])

    if tamanho_lista == 2:
        if lista[0] < lista[1]:
            return (lista[0], lista[1])
        else:
            return (lista[1], lista[0])

    metade = tamanho_lista // 2

    minimo_esquerda, maximo_esquerda = max_min_select(lista[:metade])
    minimo_direita, maximo_direita = max_min_select(lista[metade:])

    minimo_final = min(minimo_esquerda, minimo_direita)

    maximo_final = max(maximo_esquerda, maximo_direita)

    return (minimo_final, maximo_final)

if __name__ == "__main__":
    entrada_usuario = input("Digite os números da lista separados por espaço: ")
    
    lista = []
    
    items = entrada_usuario.split()

    for item in items:
        try:
            lista.append(int(item))
        except ValueError:
            print(f"Aviso: O valor '{item}' não é um número válido e será ignorado.")

    if lista:
        menor_elemento, maior_elemento = max_min_select(lista)
        print(f"\nLista processada: {lista}")
        print(f"Menor elemento encontrado: {menor_elemento}")
        print(f"Maior elemento encontrado: {maior_elemento}")
    else:
        print("\nNenhum número válido foi inserido. A lista está vazia.")
```

### Algoritmo com explicações

1. Algoritmo:

    Encontra o maior e o menor elemento em uma lista de forma simultânea utilizando a abordagem de divisão e conquista.
    Entrada: Uma lista de números (int) separados por espaço.
    Saída: Uma tupla contendo (menor_elemento, maior_elemento). Retorna (None, None) se a lista estiver vazia.
   
2. Encontra o tamanho da lista
   ```python
   tamanho_lista = len(lista)
   ```
3. Casos base

   Caso base 1: lista vazia
   ```python
   if tamanho_lista == 0:
   return (None, None)
   ```

   Caso base 2: lista com um único elemento
   ```python
   if tamanho_lista == 1:
   return (lista[0], lista[0])
   ```

   Caso base 3: lista com dois elementos. Requer apenas uma comparação. 
   ```python
   if tamanho_lista == 2:
     if lista[0] < lista[1]:
        return (lista[0], lista[1])
     else:
        return (lista[1], lista[0])
    ```
   
4. Passo de Divisão: dividir o problema em subproblemas menores.

    Resolve os subproblemas recursivamente.
    lista[:metade]: Esta é a sintaxe de "fatiamento de lista" (list slicing) do Python. Ela cria uma nova sub-lista que contém os elementos de "lista" começando do índice 0 até, mas não incluindo, o índice "metade". Esta é a metade esquerda da lista.
   
    lista[metade:]: Utilizando novamente o fatiamento, esta sintaxe cria a metade direita da lista. Ela extrai todos os elementos a partir do índice mid até o final da lista.

   ```python
   metade = tamanho_lista // 2
   
   minimo_esquerda, maximo_esquerda = max_min_select(lista[:metade])
   minimo_direita, maximo_direita = max_min_select(lista[metade:])
   ```

6. Passo de Combinação: combina os resultados dos subproblemas.
      
   Compara os mínimos das duas metades para encontrar o mínimo global.
   ```python
   minimo_final = min(minimo_esquerda, minimo_direita)
   ```

   Compara os máximos das duas metades para encontrar o máximo global.
   ```python
   maximo_final = max(maximo_esquerda, maximo_direita)
   ```
7. Bloco de Execução Principal
   
   O bloco de código sob a condição `if __name__ == "__main__":` serve como o ponto de entrada do programa.

8. Solicita a entrada do usuário
   ```python
   entrada_usuario = input("Digite os números da lista separados por espaço: ")
   ```
    
9. Processa a entrada para criar uma lista de números
   ```python
    lista = []

    items = entrada_usuario.split()
   
    for item in items:
        try:
            lista.append(int(item))
        except ValueError:
            print(f"Aviso: O valor '{item}' não é um número válido e será ignorado.")
   ```

   * O metodo split() divide a string de entrada em uma lista de strings
   * Ex: "10 5 -3" se torna ['10', '5', '-3']
   * Itera sobre cada item da lista de strings
   * Tenta converter cada string para um número (float para aceitar decimais)
   * Se a conversão falhar, informa o usuário e ignora o item inválido
    
  

12. Executa o algoritmo e exibe o resultado: 
   ```python
   if lista:
        menor_elemento, maior_elemento = max_min_select(lista)
        print(f"\nLista processada: {lista}")
        print(f"Menor elemento encontrado: {menor_elemento}")
        print(f"Maior elemento encontrado: {maior_elemento}")
   else:
        print("\nNenhum número válido foi inserido. A lista está vazia.")
   ```

## Como executar o projeto

1. Clone o repositório:
```Bash
git clone https://github.com/gabrieltinoco/Algoritmo-MaxMin-Select-em-Python.git
```
2. Navegue até o diretório do projeto:
```Bash
cd Algoritmo-De-Karatsuba-Em-Python
```
3. Execute o script Python:
```Bash
python main.py
```
4. Entrada com os números da lista (somente int) separados por espaço.


## Relatório Técnico

### O que é a Complexidade Assintótica?

A **complexidade assintótica** é uma maneira de expressar o comportamento de um algoritmo quando o tamanho da entrada tende ao infinito. Ela descreve o tempo ou espaço de execução de um algoritmo em termos do tamanho da entrada, ignorando fatores como o hardware ou o tempo de execução real. A complexidade assintótica ajuda a comparar a eficiência de diferentes algoritmos de forma mais objetiva, independentemente das condições do sistema.

#### Complexidade Assintótica Temporal do Algoritmo:



