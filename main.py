def max_min_select(lista):
    """
    Encontra o maior e o menor elemento em uma lista de forma simultânea utilizando a abordagem de divisão e conquista.

    Entrada: Uma lista de números (int) separados por espaço.
    Saída: Uma tupla contendo (menor_elemento, maior_elemento). Retorna (None, None) se a lista estiver vazia.
    """

    #Encontra o tamanho da lista
    tamanho_lista = len(lista)

    # Caso base 1: lista vazia
    if tamanho_lista == 0:
        return (None, None)

    # Caso base 2: lista com um único elemento
    if tamanho_lista == 1:
        return (lista[0], lista[0])

    # Caso base 3: lista com dois elementos. Requer apenas uma comparação.
    if tamanho_lista == 2:
        if lista[0] < lista[1]:
            return (lista[0], lista[1])
        else:
            return (lista[1], lista[0])

    # Passo de Divisão: dividir o problema em subproblemas menores.
    metade = tamanho_lista // 2

    """
    Resolve os subproblemas recursivamente.
    lista[:metade]: Esta é a sintaxe de "fatiamento de lista" (list slicing) do Python. Ela cria uma nova sub-lista que contém os elementos de "lista" começando do índice 0 até, mas não incluindo, o índice "metade". Esta é a metade esquerda da lista.
    lista[metade:]: Utilizando novamente o fatiamento, esta sintaxe cria a metade direita da lista. Ela extrai todos os elementos a partir do índice mid até o final da lista.
    """
    minimo_esquerda, maximo_esquerda = max_min_select(lista[:metade])
    minimo_direita, maximo_direita = max_min_select(lista[metade:])

    # Passo de Combinação: combina os resultados dos subproblemas.
    # Compara os mínimos das duas metades para encontrar o mínimo global.
    minimo_final = min(minimo_esquerda, minimo_direita)

    # Compara os máximos das duas metades para encontrar o máximo global.
    maximo_final = max(maximo_esquerda, maximo_direita)

    return (minimo_final, maximo_final)

# --- Exemplo de Execução ---
if __name__ == "__main__":
    # 1. Solicita a entrada do usuário
    entrada_usuario = input("Digite os números da lista separados por espaço: ")

    # 2. Processa a entrada para criar uma lista de números
    lista = []

    # O metodo split() divide a string de entrada em uma lista de strings
    # Ex: "10 5 -3" se torna ['10', '5', '-3']
    items = entrada_usuario.split()

    # Itera sobre cada item da lista de strings
    for item in items:
        try:
            # Tenta converter cada string para um número (float para aceitar decimais)
            lista.append(int(item))
        except ValueError:
            # Se a conversão falhar, informa o usuário e ignora o item inválido
            print(f"Aviso: O valor '{item}' não é um número válido e será ignorado.")

    # 3. Executa o algoritmo e exibe o resultado
    # Verifica se a lista 'lista' não está vazia após o processamento
    if lista:
        menor_elemento, maior_elemento = max_min_select(lista)
        print(f"\nLista processada: {lista}")
        print(f"Menor elemento encontrado: {menor_elemento}")
        print(f"Maior elemento encontrado: {maior_elemento}")
    else:
        # Informa ao usuário se nenhum número válido foi digitado
        print("\nNenhum número válido foi inserido. A lista está vazia.")