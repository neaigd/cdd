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
