
# Classificação Decimal de Direito (CDDir) em JSON

![Licença](https://img.shields.io/badge/licença-MIT-blue.svg) Este repositório contém a **Classificação Decimal de Direito (CDDir)**, um sistema de classificação bibliográfica para a área jurídica, em um formato JSON estruturado e de fácil utilização.

## 📖 Sobre o Projeto

A Classificação Decimal de Direito (CDDir) é um padrão amplamente utilizado em bibliotecas jurídicas no Brasil para organizar e categorizar seu acervo. Este projeto tem como objetivo principal tornar essa classificação acessível e utilizável por sistemas de software, pesquisadores e desenvolvedores, fornecendo uma versão completa em formato JSON (`classificacao.json`).

A digitalização da CDDir facilita a criação de aplicações como:
- Sistemas de busca e organização para bibliotecas digitais.
- Ferramentas de indexação de documentos jurídicos.
- APIs para consulta da estrutura do Direito.
- Análises acadêmicas sobre a organização do conhecimento jurídico.

## 🗂️ O Arquivo `classificacao.json`

O coração deste projeto é o arquivo `classificacao.json`. Ele contém a estrutura hierárquica da CDDir, permitindo que você navegue pelas categorias e subcategorias do Direito.

### Estrutura do JSON

O arquivo é um array de objetos, onde cada objeto representa uma classe (ou categoria) da CDDir e pode conter uma lista de `filhos` (subclasses).

**Exemplo de estrutura de um nó:**

```json
{
  "codigo": "341",
  "descricao": "DIREITO INTERNACIONAL PÚBLICO",
  "filhos": [
    {
      "codigo": "341.1",
      "descricao": "Personalidade internacional. Sujeitos do Direito Internacional",
      "filhos": []
    }
    // ... outras subclasses
  ]
}
````

  * `codigo`: O código numérico da classe na CDDir.
  * `descricao`: O nome por extenso da classe.
  * `filhos`: Um array contendo os objetos das subclasses diretas.

## 🚀 Como Utilizar

Você pode usar este arquivo JSON em qualquer linguagem de programação que suporte a leitura de JSON. Abaixo estão alguns exemplos básicos.

### Exemplo em Python

```python
import json

# Carrega o arquivo JSON
with open('classificacao.json', 'r', encoding='utf-8') as f:
    cdd = json.load(f)

# Função para buscar uma descrição pelo código
def buscar_por_codigo(codigo, arvore):
    for item in arvore:
        if item['codigo'] == codigo:
            return item['descricao']
        if item['filhos']:
            resultado = buscar_por_codigo(codigo, item['filhos'])
            if resultado:
                return resultado
    return "Código não encontrado"

# Exemplo de uso
codigo_procurado = "342.15"
print(f"A descrição do código {codigo_procurado} é: {buscar_por_codigo(codigo_procurado, cdd)}")
```

### Exemplo em JavaScript (Node.js)

```javascript
const fs = require('fs');

// Lê o arquivo JSON
const rawData = fs.readFileSync('classificacao.json', 'utf-8');
const cdd = JSON.parse(rawData);

// Função para buscar um item pelo código
function buscarPorCodigo(codigo, arvore) {
  for (const item of arvore) {
    if (item.codigo === codigo) {
      return item;
    }
    if (item.filhos && item.filhos.length > 0) {
      const resultado = buscarPorCodigo(codigo, item.filhos);
      if (resultado) {
        return resultado;
      }
    }
  }
  return null;
}

// Exemplo de uso
const codigoProcurado = '347.6';
const itemEncontrado = buscarPorCodigo(codigoProcurado, cdd);

if (itemEncontrado) {
  console.log(`Item encontrado:`, itemEncontrado);
} else {
  console.log(`Código ${codigoProcurado} não encontrado.`);
}
```

## 🤝 Como Contribuir

Contribuições são bem-vindas\! Se você encontrar algum erro na classificação ou tiver sugestões para melhorar a estrutura do arquivo, sinta-se à vontade para:

1.  Fazer um **Fork** deste repositório.
2.  Criar uma nova **Branch** (`git checkout -b feature/sua-melhoria`).
3.  Fazer o **Commit** de suas alterações (`git commit -m 'Adiciona/corrige X'`).
4.  Fazer o **Push** para a Branch (`git push origin feature/sua-melhoria`).
5.  Abrir um **Pull Request**.

## ⚖️ Licença

Este projeto está distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

```

---

### Próximos Passos e Dicas:

1.  **Escolha uma Licença:** Se você ainda não o fez, adicione um arquivo chamado `LICENSE` ao seu repositório. A licença MIT (sugerida no texto) é uma ótima opção para projetos abertos, pois é muito permissiva. O GitHub tem um assistente para adicionar licenças.
2.  **Ajuste a Estrutura do JSON:** O exemplo de estrutura que coloquei (`codigo`, `descricao`, `filhos`) é uma suposição. **Verifique se corresponde exatamente à estrutura do seu arquivo `classificacao.json`** e ajuste o `README` se for diferente.
3.  **Adicione um Exemplo de Uso Real:** Se você já tem um pequeno script ou projeto que usa esse JSON, considere criar uma pasta `/examples` no repositório para mostrar um caso de uso prático.

Parabéns novamente pelo projeto! Espero que esta sugestão ajude a torná-lo ainda mais acessível para a comunidade.
```
