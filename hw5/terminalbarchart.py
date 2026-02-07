"""
CMSC 14200, Winter 2026
Homework 5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from rich.console import Console
from rich.table import Table
from barchart import BarChart

class TerminalBarChart(BarChart):

    def __init__(self, data: list, year: int):

        super().__init__(data)
        self.year = year
        self.max_bar_width = 30
        self.console = Console()

    def draw(self):

        table = Table(title="Animated Bar Chart", show_header=True)
        table.add_column("Country", justify="left")
        table.add_column("Decorated Athletes", justify="right")
        
        char = "[red on red]_[/]"

        raise NotImplementedError('TerminalBarChart.draw')
        
        # return table
