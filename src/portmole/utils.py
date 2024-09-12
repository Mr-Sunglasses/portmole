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

    return subprocess.run(list(args))


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
        def wrapper():
            func()
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
