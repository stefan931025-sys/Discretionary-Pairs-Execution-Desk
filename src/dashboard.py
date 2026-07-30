from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
import pandas as pd
import numpy as np

class ExecutionDashboard:
    def __init__(self, ticker_a: str, ticker_b: str):
        self.console = Console()
        self.ticker_a = ticker_a
        self.ticker_b = ticker_b

    def render_desk(self, z_score: float, garch_vol: float, recommendation: str, position_size: float):
        table = Table(title=f"LIVE DESK: {self.ticker_a} / {self.ticker_b}", style="bold cyan")
        table.add_column("Metric", style="dim")
        table.add_column("Current Value", justify="right")
        
        table.add_row("Dynamic Z-Score", f"{z_score:.2f}")
        table.add_row("GARCH(1,1) Cond. Volatility", f"{garch_vol:.4f}")
        table.add_row("Signal / Regime", f"[bold green]{recommendation}[/bold green]" if "ENTRY" in recommendation else f"[bold yellow]{recommendation}[/bold yellow]")
        table.add_row("Suggested Allocation", f"${position_size:,.2f}")
        
        self.console.clear()
        self.console.print(Panel(table, expand=False))
