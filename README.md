# SGHSS-Backend-UNINTER-Eduardo

Este repositório contém o back-end do **Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS)**, desenvolvido como parte do Projeto Multidisciplinar do curso de Análise e Desenvolvimento de Sistemas da UNINTER – semestre 2025A1, com ênfase em back-end.

## 🩺 Objetivo

Centralizar funcionalidades críticas de gestão em ambientes hospitalares, como o cadastro de pacientes, controle de prontuários, agendamento de consultas e geração de prescrições eletrônicas. O sistema busca ser seguro, modular e aderente à LGPD, além de escalável para múltiplas unidades de saúde.

## 🧱 Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** (API RESTful)
- **PostgreSQL** (banco de dados relacional)
- **JWT (PyJWT)** (autenticação)
- **Flask-SQLAlchemy** (ORM)
- **Marshmallow** (validação)
- **Postman / Pytest / OWASP ZAP** (testes)

## 📁 Estrutura do Projeto

```
SGHSS-Backend-UNINTER-Eduardo/
│
├── app.py                  # Inicialização da API Flask
├── models.py               # Modelos de dados (ORM)
├── routes/
│   ├── auth.py             # Login e autenticação JWT
│   └── pacientes.py        # CRUD básico de pacientes
├── requirements.txt        # Dependências do projeto
└── README.md               # Instruções e descrição técnica
```

## 🚀 Como Executar Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/SeuUsuario/SGHSS-Backend-UNINTER-Eduardo.git
cd SGHSS-Backend-UNINTER-Eduardo
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python app.py
```

## 🔐 Exemplo de Requisição

**Login (POST /api/auth/login)**
```json
{
  "usuario": "admin",
  "senha": "123"
}
```

**Cadastro de Paciente (POST /api/pacientes/)**
```json
{
  "nome": "João Silva",
  "cpf": "000.000.000-00"
}
```

## 📋 Casos de Teste (sugestão)

- ✅ Login com credenciais válidas → token JWT
- ✅ Cadastro de paciente com dados válidos
- ❌ Acesso sem token → erro 401
- ❌ Consulta com paciente inexistente → erro 404

## 🧪 Ferramentas Sugeridas

- [Postman](https://www.postman.com/)
- [Pytest](https://docs.pytest.org/)
- [OWASP ZAP](https://owasp.org/www-project-zap/)
- [JMeter](https://jmeter.apache.org/)

## 📚 Projeto Acadêmico

Este projeto foi desenvolvido como atividade prática integradora da disciplina **Projeto Multidisciplinar** (ênfase em Back-End), UNINTER 2025A1.

Aluno: **Eduardo Laércio Dias**  
RU: **4556952**  

## 📎 Licença

Uso acadêmico exclusivamente. Não autorizado para ambientes de produção sem revisão e validação de segurança.
