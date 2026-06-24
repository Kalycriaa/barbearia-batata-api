# 💈 Barbearia Batata API

API REST desenvolvida com **Python**, **Flask** e **SQLAlchemy** para gerenciamento de clientes de uma barbearia.

Este projeto foi criado com o objetivo de praticar conceitos fundamentais de desenvolvimento Back-End, incluindo arquitetura em camadas, modelagem de banco de dados, separação de responsabilidades e operações CRUD.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLite
* Git e GitHub

---

## 📂 Estrutura do Projeto

```text
barbearia_batata/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
│
├── models/
│   └── barbearia_clientes.py
│
├── services/
│   └── barbearia_services.py
│
└── routes/
    └── route_clientes.py
```

### Responsabilidade de cada camada

#### Models

Responsável pela modelagem das entidades e tabelas do banco de dados.

#### Services

Responsável pelas regras de negócio da aplicação e manipulação dos dados.

#### Routes

Responsável por receber as requisições HTTP e retornar as respostas da API.

#### Database

Responsável pela configuração e inicialização do SQLAlchemy.

#### App

Responsável pela configuração principal da aplicação Flask, registro das rotas e inicialização do banco de dados.

---

## 📋 Funcionalidades

* Listar todos os clientes
* Buscar cliente por ID
* Cadastrar cliente
* Atualizar cliente
* Remover cliente

---

## 🗄️ Modelo de Dados

| Campo   | Tipo       |
| ------- | ---------- |
| id      | Integer    |
| nome    | String(50) |
| horario | String(5)  |
| data    | String(10) |

---

## 🔗 Endpoints

### Listar clientes

```http
GET /barbearia_batata
```

### Buscar cliente por ID

```http
GET /barbearia_batata/{id}
```

### Cadastrar cliente

```http
POST /barbearia_batata
```

Exemplo:

```json
{
    "nome": "Kaio Silva",
    "horario": "14:00",
    "data": "25/06/2026"
}
```

### Atualizar cliente

```http
PUT /barbearia_batata/{id}
```

### Remover cliente

```http
DELETE /barbearia_batata/{id}
```

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta do projeto

```bash
cd barbearia_batata
```

### 3. Criar ambiente virtual

```bash
python -m venv .env
```

### 4. Ativar ambiente virtual

Windows:

```bash
.env\Scripts\Activate
```

Linux/Mac:

```bash
source .env/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar aplicação

```bash
python app.py
```

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar:

* Arquitetura em Camadas
* APIs REST
* CRUD Completo
* Flask
* SQLAlchemy
* Organização de Projetos Python
* Manipulação de Banco de Dados
* Ambiente Virtual
* Git e GitHub

---

## 👨‍💻 Autor

Kaio Silva Nascimento

Estudante de Gestão da Tecnologia da Informação e desenvolvedor Back-End em formação.
