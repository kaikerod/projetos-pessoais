from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
import os

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
          console.print(f"[bold red]❌ ERRO: Saldo insuficiente para compra de R$ {valor:.2f}[/]")
          return False
      console.print(f"[bold green]✅ COMPRA: R$ {valor:.2f} aprovada com sucesso![/]")
      self._limite_disponivel -= valor
      self.valor_fatura += valor
      return True

    def pagar_fatura(self, valor):
      if valor > self.valor_fatura:
          console.print(f"[bold red]❌ ERRO: Pagamento de R$ {valor:.2f} é maior que a fatura (R$ {self.valor_fatura:.2f})[/]")
          return False
      console.print(f"[bold green]✅ PAGAMENTO: R$ {valor:.2f} realizado com sucesso![/]")
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
          console.print(f"\n[bold red]❌ ERRO: Valor de R$ {valor:.2f} excede 30% do limite total.[/]")
          return False
      self._limite_total += valor
      self._limite_disponivel += valor
      console.print(f"[bold green]✅ SUCESSO: Limite aumentado em R$ {valor:.2f}[/]\n")
      return True

    def exibir_status(self):
        table = Table(show_header=True, header_style="bold magenta", expand=True)
        table.add_column("Descrição", style="cyan")
        table.add_column("Valor", style="bold green", justify="right")
        
        table.add_row("Limite Total", f"R$ {self._limite_total:.2f}")
        table.add_row("Limite Disponível", f"R$ {self._limite_disponivel:.2f}")
        table.add_row("Fatura Atual", f"[bold red]R$ {self.valor_fatura:.2f}[/]")
        
        panel = Panel(
            table,
            title=f"💳 Resumo do Cartão: [bold yellow]{self.titular.upper()}[/]",
            border_style="cyan"
        )
        console.print(panel)
        console.print()

cartao = CartaoDeCredito("Kaike")
clear_screen()

while True:
    menu_text = (
        "[bold cyan]1.[/] Ver Status\n"
        "[bold cyan]2.[/] Comprar\n"
        "[bold cyan]3.[/] Pagar Fatura\n"
        "[bold cyan]4.[/] Aumentar Limite\n"
        "[bold cyan]5.[/] [bold red]Sair[/]"
    )
    console.print(Panel(menu_text, title="[bold blue]MENU DO CARTÃO DE CRÉDITO[/]", border_style="blue", expand=False))
    
    opcao = Prompt.ask("[bold yellow]Escolha uma opção[/]", choices=["1", "2", "3", "4", "5"])
    clear_screen()
    
    if opcao == "1":
        cartao.exibir_status()
    elif opcao == "2":
        try:
            valor_str = Prompt.ask("[bold green]Digite o valor da compra (R$)[/]")
            valor = float(valor_str)
            cartao.comprar(valor)
            console.print()
        except ValueError:
            console.print("[bold red]❌ ERRO: Digite um valor numérico válido.[/]\n")
    elif opcao == "3":
        try:
            valor_str = Prompt.ask("[bold green]Digite o valor do pagamento da fatura (R$)[/]")
            valor = float(valor_str)
            cartao.pagar_fatura(valor)
            console.print()
        except ValueError:
            console.print("[bold red]❌ ERRO: Digite um valor numérico válido.[/]\n")
    elif opcao == "4":
        try:
            valor_str = Prompt.ask("[bold green]Digite o valor do aumento de limite (R$)[/]")
            valor = float(valor_str)
            cartao.aumentar_limite(valor)
            console.print()
        except ValueError:
            console.print("[bold red]❌ ERRO: Digite um valor numérico válido.[/]\n")
    elif opcao == "5":
        console.print("[bold blue]🌟 Obrigado por usar o sistema![/]\n")
        break