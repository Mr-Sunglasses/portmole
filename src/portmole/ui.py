from rich.console import Console
from rich.table import Table


def draw_table(tabel_title: str, table_columns: list[str], table_rows: list[str] = None) -> None:
    table = Table(title=tabel_title)

    for column in table_columns:
        if table_columns[0] == column:
            table.add_column(column, justify="right",
                             style="cyan", no_wrap=True)
        elif table_columns[-1] == column:
            table.add_column(column, justify="right", style="green")
        else:
            table.add_column(column, style="magenta")

    table.add_row("Dec 20, 2019",
                  "Star Wars: The Rise of Skywalker", "$952,110,690")

    console = Console()
    console.print(table)


draw_table(tabel_title="StarWars", table_columns=[
           "Released", "Title", "Box office"])
