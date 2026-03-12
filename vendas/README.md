# 📊 Sistema de Análise de Vendas

Dashboard web para gerenciar e analisar vendas de produtos, construído com **Python/Flask** e um frontend moderno.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| **Dashboard com métricas** | Cards exibindo total de vendas, quantidade, produto mais vendido e mais lucrativo |
| **Cadastro de vendas** | Formulário para adicionar novas vendas (produto, valor, data) |
| **Listagem de vendas** | Tabela com todas as vendas registradas |
| **Filtro por valor** | Filtrar vendas acima de um valor mínimo |
| **Análise automática** | Produto mais vendido, mais lucrativo e média de vendas por dia |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório ou navegue até a pasta do projeto
cd vendas

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 📁 Estrutura do Projeto

```
vendas/
├── app.py               # Servidor Flask + classes de negócio
├── requirements.txt     # Dependências Python
├── README.md            # Documentação
└── templates/
    └── index.html       # Frontend (HTML/CSS/JS)
```

---

## 🔌 API REST

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Página principal (dashboard) |
| `GET` | `/api/vendas` | Lista todas as vendas |
| `POST` | `/api/vendas` | Adiciona uma nova venda |
| `GET` | `/api/vendas/filtro?valor_minimo=X` | Filtra vendas acima do valor |
| `GET` | `/api/analise` | Retorna métricas e análises |

### Exemplo — Adicionar Venda

```bash
curl -X POST http://localhost:5000/api/vendas \
  -H "Content-Type: application/json" \
  -d '{"produto": "Mouse", "valor": 150.00, "data_venda": "2025-03-01"}'
```

### Exemplo — Resposta da Análise (`GET /api/analise`)

```json
{
  "total_vendas": 10150.0,
  "quantidade_vendas": 6,
  "produto_mais_vendido": "Notebook",
  "produto_mais_lucrativo": "Notebook",
  "media_vendas_por_dia": 2030.0
}
```

---

## 🛠️ Tecnologias

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (vanilla), JavaScript (vanilla) — *Desenvolvido por IA*
- **Tipografia:** Google Fonts (Inter)
- **Design:** Dark theme, gradientes, micro-animações

---

## 📝 Classes Principais

### `Venda`
Representa uma venda individual com produto, valor e data.

### `AnaliseVendas`
Gerencia a lista de vendas e oferece métodos de análise:

- `adicionar_venda(venda)` — Adiciona uma venda à lista
- `vendas_acima_de(valor_minimo)` — Filtra vendas acima de um valor
- `total_vendas()` — Soma total de todas as vendas
- `total_vendas_periodo(inicio, fim)` — Total em um período específico
- `produto_mais_vendido()` — Produto com maior quantidade de vendas
- `produto_mais_lucrativo()` — Produto com maior receita total
- `media_vendas_por_dia()` — Média de valores vendidos por dia
