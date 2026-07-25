import os
import time
import glob
import json
import pandas as pd
from algoritmos.ForcaBruta import busca_forca_bruta

def gerar_caminho_saida(nome_arquivo_input, pasta="out/forcaBruta"):
    nome_sem_extensao = os.path.splitext(os.path.basename(nome_arquivo_input))[0]
    
    return os.path.join(pasta, f"resultados_{nome_sem_extensao}.csv")

def carregar_padroes(arquivo="padroes.json"):
    if not os.path.exists(arquivo):
        print(f"[ERRO] Arquivo de padrões '{arquivo}' não encontrado.")
        return []

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        if isinstance(dados, dict):
            return dados.get("padroes", [])
        if isinstance(dados, list):
            return dados

        print(f"[ERRO] Formato inesperado em '{arquivo}'.")
        return []
    except json.JSONDecodeError:
        print(f"[ERRO] Erro ao ler arquivo JSON '{arquivo}'.")
        return []

def carregar_sequencia(path):
    with open(path, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        
    if linhas and linhas[0].startswith(">"):
        linhas = linhas[1:]
        
    return "".join(linha.strip() for linha in linhas)

def rodar_experimento_forca_bruta(caminho_dna, lista_padroes, arquivo_saida="resultados_forca_bruta.csv"):
    if not os.path.exists(caminho_dna):
        print(f"[ERRO] O arquivo '{caminho_dna}' não foi encontrado.")
        return

    texto_dna = carregar_sequencia(caminho_dna)

    resultados = []
    tamanhos_permitidos = {3, 5, 10}

    for padrao in lista_padroes:
        tam = len(padrao)

        if tam not in tamanhos_permitidos:
            print(f"[ERRO] Sequências de tamanho {tam} não permitido")
            continue

        inicio = time.perf_counter()
        posicoes, comparacoes = busca_forca_bruta(texto_dna, padrao)
        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1000

        resultados.append({
            "Algoritmo": "Força Bruta",
            "Tamanho (M)": tam,
            "Padrão": padrao,
            "Total Ocorrências": len(posicoes),
            "Primeiras Posições": str(posicoes[:5]),
            "Nº Comparações": comparacoes,
            "Tempo (ms)": round(tempo_ms, 4)
        })

    if not resultados:
        print("[ERRO] Nenhum padrão válido foi processado.")
        return

    df = pd.DataFrame(resultados)
    df.to_csv(arquivo_saida, index=False, encoding="utf-8")
    print(f"[SUCESSO] {os.path.basename(caminho_dna)} → {arquivo_saida}")


if __name__ == "__main__":
    padroes_para_testar = carregar_padroes("padroes.json")

    if not padroes_para_testar:
        print("[ERRO] Nenhum padrão foi carregado.")
    else:
        pasta_input = "input"
        if os.path.exists(pasta_input):
            arquivos_input = glob.glob(os.path.join(pasta_input, "*.txt"))
            
            if arquivos_input:
                for caminho_arquivo in sorted(arquivos_input):
                    print(f"\n{'='*70}")
                    arquivo_saida = gerar_caminho_saida(caminho_arquivo)
                    rodar_experimento_forca_bruta(caminho_arquivo, padroes_para_testar, arquivo_saida)
            else:
                print(f"[ERRO] Nenhum arquivo .txt encontrado na pasta '{pasta_input}'.")
        else:
            print(f"[ERRO] A pasta '{pasta_input}' não existe.")