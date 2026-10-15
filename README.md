<img width="736" height="368" alt="TI" src="https://github.com/user-attachments/assets/50b93437-1416-446b-9318-af3b242c45a9" />

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?style=flat&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=flat&logo=requests&logoColor=white)


# 🧪 QA Automation — E-commerce com Python

Projeto criado para praticar automação de testes de software e um cenário de e-commerce, utilizando Python, Pytest, Playwright e Requests.

## Objetivo

Validar regras de negócio de um e-commerce e verificar os dados retornados por uma API de produtos.

## Tecnologias utilizadas

-**Python** — linguagem de programação.
-**Pytest** — execução e organização dos testes.
-**Playwright** — automação de testes de interface no navegador.
-**Requests** — testes de API HTTP.
-**Git e GitHub** — versionamento do código.
-**GitHub Actions** — execução automática dos testes.

## Cenários de teste

### Testes funcionais
- Adicionar produtos ao carrinho.
- Calcular o subtotal da compra.
- Aplicar cupom de desconto válido.
- Rejeitar cupom inválido.
- Validar quantidades inválidas.
- Impedir compras acima do estoque disponível.
- Impedir a finalização de um carrinho vazio.
- Validar a finalização de uma compra.

### Testes de API
- Consultar um produto por ID.
- Validar o código HTTP da resposta.
- Verificar os campos e os tipos de dados do produto.
- Listar produtos e validar a estrutura da resposta.

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/claupalomars/qa-automacao-ecommerce.git
cd qa-automacao-ecommerce
```

### 2. Criar e ativar o ambiente virtual no Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Executar os testes funcionais

```bash
python -m pytest -v
```

### 5. Executar os testes de API

```bash
python -m pytest -m integration -v
```

## 📊 Resultados validados

- 13 testes funcionais aprovados.
- 2 testes de API aprovados em execução separada.

Os resultados podem variar conforme alterações no código e a disponibilidade da API externa.

## O que pratiquei aqui

- Escrita de testes automatizados com Pytest.
- Uso de fixtures e parametrização.
- Validação de regras de negócio.
- Testes de integração com API REST.
- Verificação de status HTTP e estrutura JSON.
- Organização de código e testes em Python.

---

**Projeto educacional de portfólio em QA Automation.**
