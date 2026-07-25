def busca_forca_bruta(texto, padrao):
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    comparacoes = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparacoes += 1
            if texto[i + j] == padrao[j]:
                j += 1
            else:
                break

        if j == m:
            ocorrencias.append(i)

    return ocorrencias, comparacoes