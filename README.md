# 🎬 Flix API

API RESTful desenvolvida com **Django** e **Django REST Framework (DRF)** para gerenciamento de filmes, gêneros, atores e reviews. Este projeto faz parte do aprendizado no curso **Django Master** da PycodeBR.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.x**
- **Django**
- **Django REST Framework**
- **SQLite** (em desenvolvimento)
- **Django Admin**

---

## ✅ Funcionalidades
- **Autenticação**:
  - Registro e login de usuários
  - Geração de tokens para segurança da API
  - JWT (JSON Web Token)
  - Permissão de Usuários
- **Filmes**:
  - CRUD completo
  - Relacionamento com gêneros, atores e reviews
- **Atores**:
  - Cadastro com dados relevantes (nome, bio, data de nascimento)
- **Gêneros**:
  - Adição e gerenciamento de gêneros de filmes
- **Reviews**:
  - Usuários autenticados podem adicionar avaliações
- **API RESTful**:
  - Endpoints documentados com DRF
  - Respostas em JSON
- **Painel Administrativo**:
  - Gerenciamento via Django Admin

---

## 📂 Estrutura do Projeto
flix_api/ ├── actors/ ├── authentication/ ├── genres/ ├── movies/ ├── reviews/ ├── manage.py ├── requirements.txt └── requirements_dev.txt

---

## ▶️ Como Executar o Projeto
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/gabriel-melgaco/flix_api.git
   cd flix_api
```

2. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Realize as migrações:**
```bash
python manage.py migrate
```

5. **Crie um superusuário:**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor**:
```bash
python manage.py runserver
```


## 🔗 Endpoints Principais
- /api/v1/movies/ – Gerenciamento de filmes
- /api/v1/genres/ – Gerenciamento de gêneros
- /api/v1/actors/ – Gerenciamento de atores
- /api/v1/reviews/ – Gerenciamento de reviews
- /api/v1/movies/stats - Estatísticas de filmes
