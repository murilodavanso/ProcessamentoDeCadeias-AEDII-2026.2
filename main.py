import glob
import json
import os
import time

import pandas as pd

from algoritmos.ForcaBruta import busca_forca_bruta
from algoritmos.KMP import busca_kmp


def gerar_caminho_saida(nome_arquivo_input, pasta):
    nome_sem_extensao = os.path.splitext(
        os.path.basename(nome_arquivo_input)
    )[0]

    return os.path.join(
        pasta,
        f"resultados_{nome_sem_extensao}.csv"
    )

def carregar_padroes(arquivo="padroes.json"):
    if not os.path.exists(arquivo):
        print(f"[ERRO] Arquivo de padrões '{arquivo}' não encontrado.")
        return []

    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo_json:
            dados = json.load(arquivo_json)

        if isinstance(dados, dict):
            padroes = dados.get("padroes", [])
        elif isinstance(dados, list):
            padroes = dados
        else:
            print(f"[ERRO] Formato inesperado em '{arquivo}'.")
            return []

        return [
            padrao
            for padrao in padroes
            if isinstance(padrao, str) and padrao
        ]

    except json.JSONDecodeError:
        print(f"[ERRO] Erro ao ler arquivo JSON '{arquivo}'.")
        return []


def carregar_sequencia(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    if linhas and linhas[0].startswith(">"):
        linhas = linhas[1:]

    return "".join(linha.strip() for linha in linhas)


def rodar_experimento(
    caminho_dna,
    lista_padroes,
    algoritmo,
    nome_algoritmo,
    pasta_saida
):
    if not os.path.exists(caminho_dna):
        print(f"[ERRO] O arquivo '{caminho_dna}' não foi encontrado.")
        return

    os.makedirs(pasta_saida, exist_ok=True)

    arquivo_saida = gerar_caminho_saida(
        caminho_dna,
        pasta_saida
    )

    texto_dna = carregar_sequencia(caminho_dna)
    resultados = []

    for padrao in lista_padroes:
        inicio = time.perf_counter()

        posicoes, comparacoes = algoritmo(
            texto_dna,
            padrao
        )

        fim = time.perf_counter()
        tempo_ms = (fim - inicio) * 1000

        resultados.append({
            "Algoritmo": nome_algoritmo,
            "Tamanho Texto (N)": len(texto_dna),
            "Tamanho Padrão (M)": len(padrao),
            "Padrão": padrao,
            "Total Ocorrências": len(posicoes),
            "Primeiras Posições": str(posicoes[:5]),
            "Nº Comparações": comparacoes,
            "Tempo (ms)": round(tempo_ms, 4)
        })

    if not resultados:
        print(
            f"[ERRO] Nenhum padrão válido foi processado "
            f"por {nome_algoritmo}."
        )
        return

    dataframe = pd.DataFrame(resultados)

    dataframe.to_csv(
        arquivo_saida,
        index=False,
        encoding="utf-8"
    )

    print(
        f"[SUCESSO] {nome_algoritmo}: "
        f"{os.path.basename(caminho_dna)} -> {arquivo_saida}"
    )


def validar_resultados(texto, lista_padroes):
    """
    Confirma que os dois algoritmos encontram exatamente
    as mesmas posições.
    """
    for padrao in lista_padroes:
        posicoes_forca_bruta, _ = busca_forca_bruta(
            texto,
            padrao
        )

        posicoes_kmp, _ = busca_kmp(
            texto,
            padrao
        )

        if posicoes_forca_bruta != posicoes_kmp:
            raise ValueError(
                f"Resultados diferentes para o padrão '{padrao}': "
                f"Força Bruta={posicoes_forca_bruta[:10]}, "
                f"KMP={posicoes_kmp[:10]}"
            )


if __name__ == "__main__":
    padroes_para_testar = carregar_padroes("padroes.json")

    if not padroes_para_testar:
        print("[ERRO] Nenhum padrão foi carregado.")
    else:
        pasta_input = "input"

        if not os.path.exists(pasta_input):
            print(
                f"[ERRO] A pasta '{pasta_input}' não existe."
            )
        else:
            arquivos_input = sorted(
                glob.glob(os.path.join(pasta_input, "*.txt"))
            )

            if not arquivos_input:
                print(
                    f"[ERRO] Nenhum arquivo .txt encontrado "
                    f"na pasta '{pasta_input}'."
                )
            else:
                for caminho_arquivo in arquivos_input:
                    print(f"\n{'=' * 70}")
                    print(
                        f"Arquivo: "
                        f"{os.path.basename(caminho_arquivo)}"
                    )

                    texto_dna = carregar_sequencia(
                        caminho_arquivo
                    )

                    validar_resultados(
                        texto_dna,
                        padroes_para_testar
                    )

                    rodar_experimento(
                        caminho_dna=caminho_arquivo,
                        lista_padroes=padroes_para_testar,
                        algoritmo=busca_forca_bruta,
                        nome_algoritmo="Força Bruta",
                        pasta_saida="out/forcaBruta"
                    )

                    rodar_experimento(
                        caminho_dna=caminho_arquivo,
                        lista_padroes=padroes_para_testar,
                        algoritmo=busca_kmp,
                        nome_algoritmo="KMP",
                        pasta_saida="out/kmp"
                    )