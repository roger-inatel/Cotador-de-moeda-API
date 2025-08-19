
import typer
from rich.console import Console
from rich.table import Table
import statistics as stats
import requests

app = typer.Typer(help="Ferramenta de cotação e estatísticas")
console = Console()

@app.command()
def cotacao(valor: float, moeda_origem: str = typer.Option(..., help="Moeda de origem, ex: USD"), moeda_destino: str = typer.Option(..., help="Moeda de destino, ex: BRL")):
    """Busca cotação de moeda usando ExchangeRate API."""
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem.upper()}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if moeda_destino.upper() in dados['rates']:
            taxa = dados['rates'][moeda_destino.upper()]
            convertido = valor * taxa
            console.rule("[bold green]Cotação[/bold green]")
            console.print(f"{valor:.2f} {moeda_origem.upper()} = {convertido:.2f} {moeda_destino.upper()}", style="bold green")
        else:
            console.print(f"Moeda de destino '{moeda_destino}' não encontrada.", style="bold red")
    except Exception as e:
        console.print(f"Erro ao buscar cotação: {e}", style="bold red")

@app.command()
def stats_cmd(numeros: list[float] = typer.Argument(..., help="Lista de números para estatísticas")):
    """Calcula estatísticas simples."""
    t = Table(title="Estatísticas")
    t.add_column("Métrica", style="cyan")
    t.add_column("Valor", style="magenta")

    t.add_row("Quantidade", str(len(numeros)))
    t.add_row("Mínimo", str(min(numeros)))
    t.add_row("Máximo", str(max(numeros)))
    t.add_row("Média", f"{stats.mean(numeros):.2f}")
    t.add_row("Mediana", f"{stats.median(numeros):.2f}")

    console.print(t)

if __name__ == "__main__":
    app()
