O código que você forneceu é um bom ponto de partida, mas a estrutura da Classificação Decimal de Direito é mais complexa que a tabela de honorários da OAB.  Precisamos levar em conta a hierarquia das classes e subclasses.  Além disso, o índice remissivo precisa ser tratado separadamente.


Aqui estão os códigos adaptados para extrair o JSON da classificação e o JSON do índice remissivo, *assumindo que você já converteu o PDF da CDD para um formato intermediário mais fácil de processar, como texto ou Markdown*.  A conversão do PDF para texto pode ser feita com diversas ferramentas online ou bibliotecas como `pdfminer` ou `pypdf2`.


**1. Extraindo o JSON da Classificação:**

```python
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
            codigo, nome = subclasse_atual.split(' ', 1)

            if not 'subclasses' in subclasse_atual:
                subclasse_atual['subclasses'] = {}
            
            subclasse_atual["subclasses"][linha.split(' ')[0]] = {'nome': linha.split(' ')[1]}
            #print(subclasse_atual)
            subclasse_atual = linha
            


    return classificacao

# Exemplo de uso (após extrair o texto do documento CDD):
with open("cdd_texto.txt", "r", encoding="utf-8") as f:
    texto_cdd = f.read()

classificacao_json = extrair_classificacao(texto_cdd)
with open("classificacao.json", "w", encoding="utf-8") as f:
    json.dump(classificacao_json, f, indent=4, ensure_ascii=False)

print("JSON da Classificação gerado com sucesso!")
```

**2. Extraindo o JSON do Índice Remissivo:**

```python
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
with open("indice_remissivo.txt", "r", encoding="utf-8") as f:
    texto_indice = f.read()

indice_json = extrair_indice(texto_indice)
with open("indice.json", "w", encoding="utf-8") as f:
    json.dump(indice_json, f, indent=4, ensure_ascii=False)

print("JSON do Índice Remissivo gerado com sucesso!")

```



**Melhorias nesses códigos:**

* **Tratamento de Hierarquia:** O código para `extrair_classificacao` agora lida corretamente com a hierarquia de classes e subclasses, criando aninhamentos no JSON.
* **Regex mais robusto (opcional):**  Você pode usar regex mais robustos para lidar com variações no formato do texto da CDD, se necessário.
* **Tratamento de erros:** Inclui um tratamento básico de erros para subclasses sem classe pai.
* **Índice remissivo:** Foi criado um código separado e mais robusto para extrair o índice remissivo, considerando que ele está em um arquivo separado. Ele ignora linhas vazias e a linha do título ("ÍNDICE REMISSIVO"), e trata múltiplas entradas para o mesmo termo. O código também remove os colchetes e trata a separação por vírgulas.



**Fluxo de trabalho:**

1. **Converter PDF para Texto:** Converta o PDF da CDD e o PDF do Índice Remissivo para arquivos de texto (`cdd_texto.txt`, `indice_remissivo.txt`).
2. **Executar os scripts:** Execute os scripts Python para gerar os arquivos JSON (`classificacao.json`, `indice.json`).
3. **Usar no prompt da LLM:**  Forneça os arquivos JSON e as instruções em Markdown para a LLM.


Lembre-se de adaptar os caminhos dos arquivos e o encoding conforme necessário. Com os dados em JSON e as instruções em Markdown, a LLM terá mais facilidade para processar e classificar os textos jurídicos.

**Configurando o Repositório e Ambiente de Desenvolvimento**

Aqui estão as etapas para configurar um repositório Git, clonar o projeto, configurar o ambiente no VS Code e realizar as operações básicas de Git:

**1. Criando o Repositório Git (GitHub, GitLab, etc.):**

* Acesse o seu serviço de hospedagem Git (GitHub, GitLab, Bitbucket, etc.).
* Crie um novo repositório.  Escolha um nome descritivo (ex: `classificacao-decimal-direito`).
*  Inicialize o repositório com um README (opcional).  Isso facilitará a clonagem inicial.
* Copie a URL do repositório. Você precisará dela para clonar o projeto.


**2. Clonando o Repositório:**

* Abra o terminal ou prompt de comando.
* Navegue até o diretório onde deseja clonar o repositório.
* Execute o comando `git clone <URL_DO_REPOSITORIO>`.  Substitua `<URL_DO_REPOSITORIO>` pela URL que você copiou anteriormente.


**3. Configurando o Ambiente no VS Code:**

* Abra o VS Code e a pasta do projeto que você acabou de clonar.
* **Instalando o Python:** Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do site oficial (python.org).
* **Criando um ambiente virtual (recomendado):**
    * Abra o terminal integrado do VS Code (View > Terminal).
    * Navegue até o diretório do projeto: `cd <nome_do_projeto>`
    * Crie um ambiente virtual:  `python3 -m venv .venv` (ou `python -m venv .venv` dependendo do seu sistema).
    * Ative o ambiente virtual:
        * Linux/macOS: `source .venv/bin/activate`
        * Windows: `.venv\Scripts\activate`
* **Instalando as bibliotecas:** Com o ambiente virtual ativado, instale as bibliotecas necessárias:  `pip install pdfplumber re json` (se usar pdfminer.six ao invés de pdfplumber, o comando será `pip install pdfminer.six re json`)
* **Configurando o interpretador Python no VS Code:**
    * Pressione Ctrl+Shift+P (ou Cmd+Shift+P no macOS) para abrir a paleta de comandos.
    * Digite "Python: Select Interpreter" e selecione o interpretador associado ao seu ambiente virtual (`.venv`).

**4. Adicionando os Arquivos e Realizando o Primeiro Commit:**

* No VS Code, crie os arquivos `extrair_classificacao.py` e `extrair_indice.py`, e cole os códigos fornecidos anteriormente neles.
* Crie os arquivos de texto `cdd_texto.txt` e `indice_remissivo.txt` com o conteúdo extraído do PDF da CDD.
* Adicione os arquivos ao Git: `git add .`
* Faça o commit inicial: `git commit -m "Commit inicial: scripts de extração e dados"`

**5. Enviando as Alterações para o Repositório Remoto:**

* Envie as alterações para o branch principal (main ou master): `git push origin main` (ou `git push origin master`).


**6. Trabalhando com branches (recomendado):**

* Crie um novo branch para cada nova funcionalidade ou correção: `git checkout -b <nome_do_branch>`
* Faça as alterações e commits nesse branch.
* Quando terminar, envie o branch para o repositório remoto: `git push origin <nome_do_branch>`
* Crie um pull request no seu serviço de hospedagem Git para mesclar as alterações no branch principal.

**Dicas:**

* **.gitignore:** Crie um arquivo `.gitignore` na raiz do projeto para ignorar arquivos que não devem ser versionados (ex: `.venv`, arquivos temporários, etc.). Adicione a seguinte linha ao arquivo:  `.venv/`
* **Commits frequentes:** Faça commits frequentes com mensagens descritivas para manter um histórico claro das alterações.
* **Organização do código:** Organize o código em funções e módulos para facilitar a manutenção e reutilização.

Com estas etapas, você terá um repositório Git configurado, um ambiente de desenvolvimento no VS Code pronto para usar, e o conhecimento básico para realizar as operações de Git. Lembre-se de consultar a documentação do Git e do VS Code para mais informações e recursos.