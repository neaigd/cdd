import json
import re

def extrair_classificacao(texto_cdd):
    classificacao = {}
    classe_atual = None
    subclasse_atual = None

    for linha in texto_cdd.splitlines():
        linha = linha.strip()
        if not linha:
            continue

        match_classe = re.match(r"^(\d{3})\s+(.+)$", linha)
        match_subclasse = re.match(r"^(\d{3}\.\d+)\s+(.+)$", linha)

        if match_classe:
            codigo, nome = match_classe.groups()
            classificacao[codigo] = {"nome": nome, "subclasses": {}}
            classe_atual = classificacao[codigo]
            subclasse_atual = None

        elif match_subclasse:
            codigo, nome = match_subclasse.groups()
            if classe_atual is None:
                print(f"Subclasse {codigo} sem classe pai.")
                continue  # Ou crie uma classe "desconhecida"
            if subclasse_atual is None:
                classe_atual["subclasses"][codigo] = {"nome": nome}
            else:
                subclasse_atual['subclasses'][codigo] = {'nome': nome}

        elif "." in linha and subclasse_atual is not None:
            codigo, nome = linha.split(' ', 1)

            if 'subclasses' not in subclasse_atual:
                subclasse_atual['subclasses'] = {}

            subclasse_atual["subclasses"][linha.split(' ')[0]] = {'nome': linha.split(' ')[1]}
            subclasse_atual = linha

    return classificacao

# Exemplo de uso (após extrair o texto do documento CDD):
with open("class.txt", "r", encoding="utf-8") as f:
    texto_cdd = f.read()

classificacao_json = extrair_classificacao(texto_cdd)

with open("classificacao.json", "w", encoding="utf-8") as f:
    json.dump(classificacao_json, f, indent=4, ensure_ascii=False)

print("JSON da Classificação gerado com sucesso!")