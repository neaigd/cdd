import json
import re


def extrair_indice(texto_indice):
    indice_remissivo = {}
    for linha in texto_indice.splitlines():
        linha = linha.strip()
        if not linha or 'ÍNDICE REMISSIVO' in linha or linha == ' ': #remover linhas vazias, com INDICE REMISSIVO ou apenas com espaço
           continue

        partes = linha.split(" ", 1)

        assunto = partes[0]
        if len(partes) > 1:
            classificacoes = []
            numeros = partes[1].replace('[', '').replace(']', '').split(', ')
            for numero in numeros:
                classificacoes.append(numero)

            indice_remissivo[assunto] = classificacoes
        else:
            indice_remissivo[assunto] = [partes[0]]


    return indice_remissivo

# Exemplo de uso (após extrair o texto do índice remissivo):
with open("indice.txt", "r", encoding="utf-8") as f:
    texto_indice = f.read()

indice_json = extrair_indice(texto_indice)
with open("indice.json", "w", encoding="utf-8") as f:
    json.dump(indice_json, f, indent=4, ensure_ascii=False)

print("JSON do Índice Remissivo gerado com sucesso!")
