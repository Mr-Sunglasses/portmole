from rich.console import Console
from rich.table import Table
from portmole.utils import draw_port_command_column_data, draw_port_command_rows_data, ping_after_seconds


@ping_after_seconds(30)
def draw_table(table_title: str, table_columns: list[str], table_rows: list[list[str]]) -> None:
    table = Table(title=table_title)

    for column in table_columns:
        if table_columns[0] == column:
            table.add_column(column, justify="right",
                             style="cyan", no_wrap=True)
        elif table_columns[-1] == column:
            table.add_column(column, justify="right", style="green")
        else:
            table.add_column(column, style="magenta")

    for row in table_rows:
        table.add_row(*row)

    console = Console()
    console.print(table)


while True:
    draw_table(table_title="Occupied Ports 🐇🧐🔍 ", table_columns=draw_port_command_column_data(),
               table_rows=draw_port_command_rows_data())

# draw_table(table_title="Occupied Ports 🐇🧐🔍", table_columns=draw_port_command_column_data(),
#            table_rows=draw_port_command_rows_data())
