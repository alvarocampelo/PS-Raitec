# 🏨 Sistema de Gestão Hoteleira
### Processo Seletivo RAITec

> Um sistema abrangente de gestão hoteleira desenvolvido em **Python** e **MySQL**. A aplicação oferece funcionalidades para o cadastro de clientes, o gerenciamento de quartos e a operação de reservas, incluindo controles administrativos.

---

## 📋 Funcionalidades

### 👤 Gerenciamento de Clientes
- Cadastro de clientes com validação de CPF, nome e idade
- Autenticação de clientes via CPF
- Visualização do histórico de reservas pessoais
- Solicitação de novas reservas
- Cancelamento de reservas pendentes

### 🛏️ Gerenciamento de Quartos
- Cadastro de novos quartos com definição de capacidade e valor da diária
- Visualização de quartos disponíveis
- Monitoramento do status de ocupação dos quartos
- Exclusão de quartos do sistema

### 📅 Sistema de Reservas
- Fluxo completo de reservas (solicitação, check-in e check-out)
- Detecção e prevenção de conflito de datas
- Cálculo automático de preços com base no período da estadia
- Monitoramento do status da reserva (pendente ou ativa)
- Cancelamento de reservas anterior ao check-in

### 🔐 Painel Administrativo
- Autenticação segura com proteção por senha
- Operações completas de **CRUD** (Criação, Leitura, Atualização e Exclusão) para quartos, clientes e reservas
- Gerenciamento dos processos de check-in e check-out
- Visualização de todas as reservas com a totalização de valores calculada
- Rastreamento individualizado de reservas por cliente

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| **Python 3.x** | Linguagem principal |
| **MySQL** | Banco de dados relacional |
| **Aiven Cloud** | Hospedagem do banco com conexão SSL |
| **Arquitetura MVC** | Model-View-Controller |

---

## 📦 Bibliotecas Adicionais

Instale as dependências via terminal com `pip install <biblioteca>`:

```bash
pip install mysql-connector-python
pip install python-dotenv
```

| Biblioteca | Finalidade |
|---|---|
| `mysql-connector-python` | Conectividade com o banco de dados |
| `python-dotenv` | Gerenciamento de variáveis de ambiente |

---

## 📁 Estrutura do Projeto

```
hotel_sistemas/
│
├── controllers/
│   └── hotel_controller.py     # Lógica de controle da aplicação (MVC)
│
├── data/                       # Dados auxiliares ou scripts de seed
│
├── models/
│   ├── admin.py                # Model do administrador
│   ├── booking.py              # Model de reservas
│   ├── client.py               # Model de clientes
│   └── room.py                 # Model de quartos
│
├── repository/                 # Camada de acesso ao banco de dados
│
├── ui/
│   └── menu.py                 # Interface de menus no terminal
│
├── .env                        # Variáveis de ambiente (não versionar)
├── ca.pem                      # Certificado SSL para conexão Aiven
├── main.py                     # Ponto de entrada da aplicação
└── teste.py                    # Scripts de teste
```

---

## ⚙️ Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
DB_HOST=seu-host.aivencloud.com
DB_PORT=18818
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_NAME=defaultdb
```

> ⚠️ **Atenção:** Nunca versione o arquivo `.env` com dados sensíveis. Adicione-o ao `.gitignore`.

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/hotel-sistemas.git

# Acesse o diretório
cd hotel-sistemas

# Instale as dependências
pip install mysql-connector-python python-dotenv

# Configure o arquivo .env com suas credenciais

# Execute a aplicação
python main.py
```

---

<p align="center">Desenvolvido para o Processo Seletivo <strong>RAITec</strong></p>
