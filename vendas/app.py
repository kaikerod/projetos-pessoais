from datetime import date, datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Venda:
  def __init__(self, produto, valor, data_venda):
    self.produto = produto
    self.valor = valor
    self.data_venda = data_venda

  def to_dict(self):
    return {
      "produto": self.produto,
      "valor": self.valor,
      "data_venda": self.data_venda.strftime('%d/%m/%Y')
    }

  def __str__(self):
    return f"Produto: {self.produto:<15} | Valor: R$ {self.valor:<7.2f} | Data: {self.data_venda.strftime('%d/%m/%Y')}"

class AnaliseVendas:
  def __init__(self):
    self.lista_vendas = []

  def adicionar_venda(self, venda):
    self.lista_vendas.append(venda)

  def vendas_acima_de(self, valor_minimo):
    vendas_filtradas = [venda for venda in self.lista_vendas if venda.valor > valor_minimo]
    return vendas_filtradas

  def total_vendas_periodo(self, data_inicio, data_fim):
    total = sum(venda.valor for venda in self.lista_vendas if data_inicio <= venda.data_venda <= data_fim)
    return total

  def total_vendas(self):
    return sum(venda.valor for venda in self.lista_vendas)

  def produto_mais_vendido(self):
    if not self.lista_vendas:
      return None
    
    contagem_produtos = {}
    for venda in self.lista_vendas:
      nome_produto = venda.produto
      if nome_produto in contagem_produtos:
        contagem_produtos[nome_produto] += 1
      else:
        contagem_produtos[nome_produto] = 1
    
    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    return produto_mais_vendido

  def produto_mais_lucrativo(self):
    if not self.lista_vendas:
      return None
    
    lucro_produtos = {}
    for venda in self.lista_vendas:
      nome_produto = venda.produto
      if nome_produto in lucro_produtos:
        lucro_produtos[nome_produto] += venda.valor
      else:
        lucro_produtos[nome_produto] = venda.valor
    
    produto_mais_lucrativo = max(lucro_produtos, key=lucro_produtos.get)
    return produto_mais_lucrativo

  def media_vendas_por_dia(self):
    if not self.lista_vendas:
      return None
    
    vendas_por_dia = {}
    for venda in self.lista_vendas:
      data = venda.data_venda
      if data in vendas_por_dia:
        vendas_por_dia[data] += venda.valor
      else:
        vendas_por_dia[data] = venda.valor
    
    media_vendas_por_dia = sum(vendas_por_dia.values()) / len(vendas_por_dia)
    return media_vendas_por_dia


# Instância global
meu_sistema = AnaliseVendas()

# Vendas de exemplo
v1 = Venda('Notebook', 2500.00, date(2025, 2, 28))
v2 = Venda('Smartphone', 1500.00, date(2025, 12, 25))
v3 = Venda('Tablet', 1000.00, date(2025, 1, 1))
v4 = Venda('Notebook', 2500.00, date(2025, 3, 15))
v5 = Venda('Monitor', 1800.00, date(2025, 6, 10))
v6 = Venda('Teclado', 350.00, date(2025, 7, 20))

for v in [v1, v2, v3, v4, v5, v6]:
  meu_sistema.adicionar_venda(v)


# ─── Rotas ────────────────────────────────────────────

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/api/vendas', methods=['GET'])
def listar_vendas():
  vendas = [v.to_dict() for v in meu_sistema.lista_vendas]
  return jsonify(vendas)


@app.route('/api/vendas', methods=['POST'])
def adicionar_venda():
  dados = request.get_json()
  try:
    produto = dados['produto']
    valor = float(dados['valor'])
    data_venda = datetime.strptime(dados['data_venda'], '%Y-%m-%d').date()
    nova_venda = Venda(produto, valor, data_venda)
    meu_sistema.adicionar_venda(nova_venda)
    return jsonify({"mensagem": "Venda adicionada com sucesso!", "venda": nova_venda.to_dict()}), 201
  except (KeyError, ValueError) as e:
    return jsonify({"erro": f"Dados inválidos: {str(e)}"}), 400


@app.route('/api/vendas/filtro', methods=['GET'])
def filtrar_vendas():
  valor_minimo = request.args.get('valor_minimo', 0, type=float)
  vendas = [v.to_dict() for v in meu_sistema.vendas_acima_de(valor_minimo)]
  return jsonify(vendas)


@app.route('/api/analise', methods=['GET'])
def analise():
  return jsonify({
    "total_vendas": meu_sistema.total_vendas(),
    "quantidade_vendas": len(meu_sistema.lista_vendas),
    "produto_mais_vendido": meu_sistema.produto_mais_vendido(),
    "produto_mais_lucrativo": meu_sistema.produto_mais_lucrativo(),
    "media_vendas_por_dia": round(meu_sistema.media_vendas_por_dia(), 2) if meu_sistema.media_vendas_por_dia() else 0
  })


if __name__ == '__main__':
  app.run(debug=True, port=5000)