# 💳 Simulador de Cartão de Crédito

Este é um projeto simples em Python que simula o gerenciamento de um cartão de crédito via terminal. A aplicação utiliza a biblioteca **Rich** para proporcionar uma interface de usuário elegante, colorida e interativa diretamente no console.

## 🚀 Funcionalidades

- **Consulta de Status:** Visualize de forma clara o seu limite total, limite disponível e o valor atual da fatura.
- **Realização de Compras:** Simule compras abatendo o valor do limite disponível e aumentando a fatura.
- **Pagamento de Fatura:** Realize o pagamento total ou parcial da fatura para reestabelecer seu limite.
- **Solicitação de Aumento de Limite:** Tente aumentar seu limite total (com regras de negócio baseadas no uso).
- **Extrato Detalhado:** Acompanhe o histórico completo de transações (compras e pagamentos) em uma tabela organizada.
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
