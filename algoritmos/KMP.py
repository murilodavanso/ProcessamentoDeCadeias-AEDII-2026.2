def construir_lps(padrao):
    """
    Constrói o vetor LPS (Longest Prefix Suffix).

    lps[i] representa o tamanho do maior prefixo próprio de padrão
    que também é sufixo do trecho padrão[0:i + 1].
    """
    m = len(padrao)
    lps = [0] * m

    comprimento = 0
    i = 1
    comparacoes = 0

    while i < m:
        comparacoes += 1

        if padrao[i] == padrao[comprimento]:
            comprimento += 1
            lps[i] = comprimento
            i += 1
        elif comprimento > 0:
            comprimento = lps[comprimento - 1]
        else:
            lps[i] = 0
            i += 1

    return lps, comparacoes


def busca_kmp(texto, padrao):
    """
    Busca todas as ocorrências de padrão em texto utilizando KMP.

    Retorna:
        ocorrencias: posições iniciais das ocorrências;
        comparacoes: total de comparações de caracteres realizadas,
        incluindo a construção do vetor LPS.
    """
    n = len(texto)
    m = len(padrao)

    if m == 0 or m > n:
        return [], 0

    lps, comparacoes = construir_lps(padrao)
    ocorrencias = []

    i = 0  # índice no texto
    j = 0  # índice no padrão

    while i < n:
        comparacoes += 1

        if texto[i] == padrao[j]:
            i += 1
            j += 1

            if j == m:
                ocorrencias.append(i - m)
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return ocorrencias, comparacoes