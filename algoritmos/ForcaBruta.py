def busca_forca_bruta(texto, padrao):
    """
    Executa a busca de um padrão de tamanho variável (3, 5, 10, etc.)
    em um texto utilizando o algoritmo de Força Bruta.
    
    Retorna:
    - ocorrencias: lista com os índices de início onde o padrão foi encontrado.
    - comparacoes: total de comparações entre caracteres efetuadas.
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    comparacoes = 0

    # Percorre o texto até a última posição válida onde o padrão cabe [cite: 17, 104]
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j += 1
            else:
                break
        
        # Se encontrou todas as letras do padrão [cite: 17, 104]
        if j == m:
            ocorrencias.append(i)

    return ocorrencias, comparacoes