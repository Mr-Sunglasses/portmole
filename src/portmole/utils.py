import subprocess
import time
from functools import wraps
import sys

CHECK_PORT_COMMAND: list["str"] = ["lsof", "-i", "-P", "-n", "-sTCP:LISTEN"]


def run_command(*args: str) -> subprocess.CompletedProcess:
    """
    Runs a command with the given arguments.

    Args:
        *args: Variable number of string arguments representing the command and its arguments.

    Returns:
        subprocess.CompletedProcess: The completed process object, which contains information about the command's execution.
    """

    return subprocess.run(list(args), capture_output=True, text=True)


def ping_after_seconds(refresh_in_seconds: int):
    """
    Decorator function to delay the execution of a function by a specified number of seconds.

    Args:
        seconds (int): The number of seconds to delay the execution.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            for i in range(refresh_in_seconds, 0, -1):
                print(f"\rRefresh in {i} seconds.....", end="")
                sys.stdout.flush()
                time.sleep(1)
            run_command("clear")
        return wrapper
    return decorator


@ping_after_seconds(10)
def get_port_out() -> None:
    print(run_command(*CHECK_PORT_COMMAND))


def draw_port_command_column_data() -> list[str]:
    """
    Returns a list of column headers for the port command data.

    Args:
        None

    Return:
        list[str]: A list of column headers, including the added "STATE" column.
    """

    result = run_command(*CHECK_PORT_COMMAND).stdout.split("\n")[0].split(" ")
    result = list(filter(None, result))
    result.append("STATE")
    return result


def draw_port_command_rows_data() -> list[list[str]]:
    """
    Returns a list of rows for the port command data, excluding the header row and empty rows.

    Args:
        None

    Return:
        list[list[str]]: A list of rows, where each row is a list of strings representing the data for that row.
    """

    result = run_command(*CHECK_PORT_COMMAND).stdout.split("\n")
    data = []
    for i in range(1, len(result)):
        data_unfiltered = result[i].split(" ")
        data_filtered = [x for x in data_unfiltered if x]
        data.append(data_filtered)

    empty_indices = [index for index,
                     sublist in enumerate(data) if not sublist]

    for empty in empty_indices:
        data.pop(empty)

    return data


# print(draw_port_command_column_data())

# print(draw_port_command_rows_data())

# print(port_command_headers())


# x = run_command(*CHECK_PORT_COMMAND)
# print(x.stdout)
# split: str = x.stdout
# list_split = split.split("\n")

# data = []

# for i in range(1, len(list_split)):
#     data_uf = list_split[i].split(" ")
#     data_filter = [x for x in data_uf if x]
#     data.append(data_filter)

# print(data)
# print(list_split[1])
# # Index_of_Zero = list_split[0].split(" ")
# Index_of_Zero = run_command(
#     *CHECK_PORT_COMMAND).stdout.split("\n")[0].split(" ")
# filter_list = [x for x in Index_of_Zero if x]
# print(filter_list)
# print(type(filter_list))
