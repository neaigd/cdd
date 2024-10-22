import re
import yaml

def parse_indice_to_yaml(file_path):
    # Estrutura para armazenar o índice
    indice = {}
    
    # Função auxiliar para inserir itens de forma hierárquica
    def insert_into_dict(d, keys, value):
        for key in keys[:-1]:
            d = d.setdefault(key, {})
        d[keys[-1]] = value

    # Variáveis para armazenar o contexto
    current_context = []
    last_key_without_code = None

    # Lê o arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()

            # Verifica se a linha tem um número de classificação
            match = re.match(r'^(.+)\s+(\d+\.\d+)$', line)
            if match:
                title, code = match.groups()
                indent_level = (len(line) - len(line.lstrip())) // 4
                
                # Atualiza o contexto de hierarquia
                current_context = current_context[:indent_level]
                
                if last_key_without_code:
                    # Se houver uma chave anterior sem código, associamos o código a ela
                    current_context.append(last_key_without_code)
                    insert_into_dict(indice, current_context, {title.strip(): code})
                    last_key_without_code = None
                else:
                    # Insere o código associado na hierarquia
                    current_context.append(title.strip())
                    insert_into_dict(indice, current_context, code)

            else:
                # Linha sem código, atualiza o contexto de hierarquia
                indent_level = (len(line) - len(line.lstrip())) // 4
                title = line.strip()

                # Atualiza a última chave sem código
                if indent_level <= len(current_context):
                    # Quando encontramos uma nova chave, reinicia o contexto a partir deste ponto
                    current_context = current_context[:indent_level]
                
                # Atribui a nova chave sem código ao contexto
                last_key_without_code = title
                current_context.append(last_key_without_code)

    # Converte a estrutura em YAML
    yaml_output = yaml.dump(indice, allow_unicode=True, sort_keys=False)

    # Salva o resultado em um novo arquivo YAML
    with open('indice.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml_file.write(yaml_output)

# Caminho do arquivo de entrada
file_path = 'indice.txt'
parse_indice_to_yaml(file_path)
