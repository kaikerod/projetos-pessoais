Este é um projeto simples em Python que simula o gerenciamento de um cartão de crédito via terminal.

### [✨ Veja a demonstração do Terminal no Navegador ✨](demo_terminal.html)

A aplicação utiliza a biblioteca **Rich** para proporcionar uma interface de usuário elegante, colorida e interativa diretamente no console.

## 🚀 Funcionalidades

- **Consulta de Status:** Visualize de forma clara o seu limite total, limite disponível e o valor atual da fatura.
- **Realização de Compras com Categorias:** Simule compras escolhendo entre categorias (Alimentação, Saúde, Mercado, etc.) para melhor organização.
- **Pagamento de Fatura:** Realize o pagamento total ou parcial da fatura para reestabelecer seu limite.
- **Solicitação de Aumento de Limite:** Tente aumentar seu limite total (com regras de negócio baseadas no uso).
- **Extrato Detalhado:** Acompanhe o histórico completo de transações em uma tabela organizada.
- **Visualização por Categoria:** Veja seus gastos agrupados por categoria com subtotais automáticos para cada uma.
- **Interface Interativa:** Menu intuitivo com feedbacks coloridos para erros e sucessos.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Rich:** Para estilização do terminal, tabelas, painéis e prompts.

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar a biblioteca `rich`.

```bash
pip install rich
```

## 🏃 Como Executar

1. Clone o repositório ou baixe o arquivo `app.py`.
2. Navegue até a pasta do projeto no terminal.
3. Execute o comando:

```bash
python app.py
```

## ⚖️ Regras de Negócio (Aumento de Limite)

Para manter o simulador realista, foram implementadas algumas condições para a aprovação do aumento de limite:
1. **Uso Mínimo:** É necessário ter consumido pelo menos **80%** do seu limite total atual para estar elegível.
2. **Valor Máximo:** O valor do aumento solicitado não pode exceder **30%** do seu limite total atual.

## 👤 Autor

Desenvolvido por **Kaike**.

---

# 💳 Credit Card Simulator

This is a simple Python project that simulates credit card management via the terminal.

### [✨ Check the Terminal Demo in your Browser ✨](demo_terminal.html)

The application uses the **Rich** library to provide an elegant, colorful, and interactive user interface directly in the console.

## 🚀 Features

- **Status Check:** Clearly visualize your total limit, available limit, and current statement balance.
- **Purchases with Categories:** Simulate purchases by choosing from categories (Food, Health, Grocery, etc.) for better organization.
- **Statement Payment:** Make a full or partial payment of your statement to restore your limit.
- **Limit Increase Request:** Attempt to increase your total limit (with business rules based on usage).
- **Detailed Statement:** Track the full transaction history in an organized table.
- **Visualization by Category:** View your spending grouped by category with automatic subtotals for each.
- **Interactive Interface:** Intuitive menu with colorful feedback for errors and successes.

## 🛠️ Technologies Used

- **Python 3.x**
- **Rich:** For terminal styling, tables, panels, and prompts.

## 📋 Prerequisites

Ensure you have Python installed on your machine. You will also need to install the `rich` library.

```bash
pip install rich
```

## 🏃 How to Run

1. Clone the repository or download the `app.py` file.
2. Navigate to the project folder in the terminal.
3. Run the command:

```bash
python app.py
```

## ⚖️ Business Rules (Limit Increase)

To keep the simulator realistic, some conditions were implemented for limit increase approval:
1. **Minimum Usage:** You must have consumed at least **80%** of your current total limit to be eligible.
2. **Maximum Value:** The requested increase cannot exceed **30%** of your current total limit.

## 👤 Author

Developed by **Kaike**.
