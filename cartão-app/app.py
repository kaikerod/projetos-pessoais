class CartaoDeCredito:
    def __init__(self, titular):
        self.titular = titular
        self._limite_total = 2500
        self._limite_disponivel = 2500
        self.valor_fatura = 0

    def __str__(self):
      return f"Cartão de Crédito de {self.titular}"
    
    @property
    def ver_limite_disponivel(self):
      return f'Limite disponível: R$ {self._limite_disponivel:.2f}'

    def comprar(self, valor):
      if valor > self._limite_disponivel:
          print(f"[ERRO] Saldo insuficiente para compra de R$ {valor:.2f}")
          return False
      print(f"[COMPRA] R$ {valor:.2f} aprovada com sucesso!")
      self._limite_disponivel -= valor
      self.valor_fatura += valor
      return True

    def pagar_fatura(self, valor):
      if valor > self.valor_fatura:
          print(f"[ERRO] Pagamento de R$ {valor:.2f} é maior que a fatura (R$ {self.valor_fatura:.2f})")
          return False
      print(f"[PAGAMENTO] R$ {valor:.2f} realizado com sucesso!")
      self.valor_fatura -= valor
      self._limite_disponivel += valor
      return True

    @property
    def ver_fatura(self):
      return f'Fatura atual: R$ {self.valor_fatura:.2f}'

    @property
    def ver_limite_total(self):
      return f'Limite total: R$ {self._limite_total:.2f}'

    def aumentar_limite(self, valor):
      if valor > self._limite_total * 0.3:
          print(f"\n[ERRO] Valor de R$ {valor:.2f} excede 30% do limite total.")
          return False
      self._limite_total += valor
      self._limite_disponivel += valor
      print(f"[SUCESSO] Limite aumentado em R$ {valor:.2f}\n")
      return True

    def exibir_status(self):
        print("-" * 30)
        print(f"RESUMO DO CARTÃO: {self.titular.upper()}")
        print("-" * 30)
        print(f"• Limite Total:      R$ {self._limite_total:>8.2f}")
        print(f"• Limite Disponível: R$ {self._limite_disponivel:>8.2f}")
        print(f"• Fatura Atual:      R$ {self.valor_fatura:>8.2f}")
        print("-" * 30 + "\n")

cartao = CartaoDeCredito("Kaike")

while True:
    print("\n" + "=" * 30)
    print("MENU DO CARTÃO DE CRÉDITO")
    print("=" * 30)
    print("1. Ver Status")
    print("2. Comprar")
    print("3. Pagar Fatura")
    print("4. Aumentar Limite")
    print("5. Sair")
    print("-" * 30)
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cartao.exibir_status()
    elif opcao == "2":
        valor = float(input("Digite o valor da compra: R$ "))
        cartao.comprar(valor)
    elif opcao == "3":
        valor = float(input("Digite o valor da fatura: R$ "))
        cartao.pagar_fatura(valor)
    elif opcao == "4":
        valor = float(input("Digite o valor do aumento: R$ "))
        cartao.aumentar_limite(valor)
    elif opcao == "5":
        print("\nObrigado por usar o sistema!")
        break
    else:
        print("[ERRO] Opção inválida. Tente novamente.")