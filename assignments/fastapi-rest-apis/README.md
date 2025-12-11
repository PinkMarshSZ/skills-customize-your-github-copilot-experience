# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Os estudantes irão construir uma API REST simples usando o framework FastAPI. A tarefa cobre definição de rotas, modelos Pydantic, tratamento de dados e execução local do servidor.

## 📝 Tasks

### 🛠️ 1. Criar Endpoints Básicos

#### Description
Implemente endpoints para listar, recuperar e criar recursos simples (ex.: itens).

#### Requirements
Completed program should:

- Expor um endpoint `GET /` que retorne uma mensagem de boas-vindas.
- Expor um endpoint `GET /items/{id}` que retorne um item por `id`.
- Expor um endpoint `POST /items/` que crie um novo item com validação usando `Pydantic`.

### 🛠️ 2. Documentação Automática

#### Description
Verifique a documentação automática gerada pelo FastAPI (Swagger UI).

#### Requirements

- A documentação Swagger deve estar disponível em `/docs`.
- Os modelos Pydantic devem incluir tipos e descrições claras.

### 🛠️ 3. Teste Manual

#### Description
Teste os endpoints com `curl` ou com o navegador (Swagger UI).

#### Requirements

- Demonstrar que é possível criar e recuperar itens.
- Incluir instruções de execução local no arquivo `starter-code.py`.

## 🧰 Entregáveis

- Código fonte em `starter-code.py` dentro da pasta da tarefa.
- Um pequeno README (este arquivo) com instruções e requisitos cumpridos.

## Duração e Data de Entrega

Data de entrega: 2025-12-18

---

Boa sorte! Se precisar, peça ajuda para adicionar testes automatizados ou um `requirements.txt`.
