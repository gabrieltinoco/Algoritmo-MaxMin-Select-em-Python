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
cd Algoritmo-MaxMin-Select-em-Python
```
3. Execute o script Python:
```Bash
python main.py
```
4. Entrada com os números da lista (somente int) separados por espaço.


## Relatório Técnico

### O que é a Complexidade Assintótica?

A **complexidade assintótica** é uma maneira de expressar o comportamento de um algoritmo quando o tamanho da entrada tende ao infinito. Ela descreve o tempo ou espaço de execução de um algoritmo em termos do tamanho da entrada, ignorando fatores como o hardware ou o tempo de execução real. A complexidade assintótica ajuda a comparar a eficiência de diferentes algoritmos de forma mais objetiva, independentemente das condições do sistema.

### **Complexidade Assintótica do Algoritmo pelo método de contagem de operações:**

Para determinar a complexidade, analisamos a operação dominante do algoritmo, que é a **comparação** entre elementos. Seja $C(n)$ o número de comparações realizadas para uma lista de $n$ elementos.

#### Etapas do Algoritmo e suas Comparações:
1.  **Casos Base:**
    * Se a lista tem 0 ou 1 elemento (`tamanho_lista <= 1`), o algoritmo não realiza nenhuma comparação. Portanto, $C(1) = 0$.
    * Se a lista tem 2 elementos (`tamanho_lista == 2`), o código executa `if lista[0] < lista[1]:`, realizando exatamente **1 comparação**. Portanto, $C(2) = 1$.

2.  **Divisão e Conquista (n > 2):**
    * **Divisão:** A lista é dividida em duas metades, `lista[:metade]` e `lista[metade:]`. Esta operação não envolve comparações entre elementos da lista.
    * **Chamadas Recursivas:** O algoritmo é chamado recursivamente para cada metade. O custo em comparações para resolver esses subproblemas é de $2 \cdot C(n/2)$.
    * **Combinação:** Após o retorno das chamadas recursivas, duas comparações são feitas para encontrar o resultado final:
        * `min(minimo_esquerda, minimo_direita)`: 1 comparação.
        * `max(maximo_esquerda, maximo_direita)`: 1 comparação.
        O custo da combinação é de **2 comparações**.

#### Cálculo do Total de Comparações:

A análise nos leva à seguinte relação de recorrência para o número de comparações:

$$C(n) = 2C(n/2) + 2$$

Para resolver essa recorrência (assumindo $n$ como potência de 2 para simplificar e usando o caso base $C(2)=1$):

$$C(n) = 2(2C(n/4) + 2) + 2 = 4C(n/4) + 4 + 2$$ 
$$C(n) = 4(2C(n/8) + 2) + 6 = 8C(n/8) + 8 + 6$$

Expandindo até o caso base $C(2)=1$, a fórmula se resolve para:

$$C(n) = \frac{n}{2} \cdot C(2) + 2(\frac{n}{2} - 1) = \frac{n}{2} + n - 2 = \frac{3n}{2} - 2$$

O número total de comparações é $\frac{3n}{2} - 2$. Como o número de operações cresce linearmente com o tamanho da entrada $n$, a complexidade temporal do algoritmo é **$O(n)$**.

### **Análise da complexidade assintótica pela aplicação do Teorema Mestre**

A recorrência que descreve o tempo de execução do algoritmo `max_min_select` é:

$$T(n) = 2T(n/2) + O(1)$$

Onde $2T(n/2)$ representa as duas chamadas recursivas em metades da lista e $O(1)$ representa o trabalho constante de divisão e combinação (as duas comparações).

A seguir, respondemos às perguntas com base na fórmula geral do Teorema Mestre: $T(n) = a \cdot T(n/b) + f(n)$.

1.  **Identifique os valores de $a$, $b$ e $f(n)$ na fórmula:**
    * **$a = 2$**: É o número de subproblemas gerados a cada chamada recursiva.
    * **$b = 2$**: É o fator pelo qual o tamanho da entrada é reduzido em cada subproblema (a lista é dividida por 2).
    * **$f(n) = O(1)$**: É o custo do trabalho realizado fora das chamadas recursivas (divisão e combinação), que é constante e não depende de $n$.

2.  **Calcule $\log_b a$ para determinar o valor de $p$:**
   
    * $p = \log_b a = \log_2 2 = 1$

4.  **Determine em qual dos três casos do Teorema Mestre esta recorrência se enquadra:**
   
    * Precisamos comparar $f(n)$ com $n^p$, que é $n^1$.
    * Temos $f(n) = O(1)$.
    * A condição do **Caso 1** do Teorema Mestre é $f(n) = O(n^{p - \epsilon})$ para algum $\epsilon > 0$.
    * Se escolhermos $\epsilon = 1$, temos $n^{p-\epsilon} = n^{1-1} = n^0 = 1$. A condição se torna $f(n) = O(1)$, o que é verdade.
    * Portanto, a recorrência se enquadra no **Caso 1** do Teorema Mestre.

6.  **Encontre a solução assintótica $T(n)$ da fórmula:**
   
    * Pelo Caso 1 do Teorema Mestre, a solução da recorrência é $T(n) = \Theta(n^p)$.
    * Substituindo $p=1$, a solução assintótica é:
        $$T(n) = \Theta(n^1) = \Theta(n)$$

Ambos os métodos confirmam que o algoritmo possui uma complexidade de tempo linear, sendo altamente eficiente para encontrar o mínimo e o máximo de uma sequência.


