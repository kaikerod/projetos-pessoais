class CartaoDeCredito:
    def __init__(self, titular, limite_total, limite_disponivel, valor_fatura):
        self.titular = titular
        self.limite_total = limite_total
        self._limite_disponivel = limite_disponivel
        self.valor_fatura = valor_fatura

    def __str__(self):
      return f"Cartão de Crédito de {self.titular}"
    
    @property
    def limite_disponivel(self):
      return self._limite_disponivel

    def comprar(self, valor):
      if valor > self._limite_disponivel:
          print("Erro: Saldo insuficiente")
          return False
      self._limite_disponivel -= valor
      self.valor_fatura += valor
      return True
