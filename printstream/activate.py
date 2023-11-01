import builtins
import sys
import inspect
from termcolor import colored
from .config import get_config

# Store the original print function for restoration later
_original_print = builtins.print


def custom_print(*args, **kwargs):
    config = get_config()
    level = config["level"]
    if level == -1:
        _original_print(*args, **kwargs)
    elif level == 0:
        _original_print(*args, **kwargs)
    elif level == 1:
        frame = inspect.currentframe().f_back
        func_name = frame.f_code.co_name

        # Colorize function name based on hash
        if config["colorize"]:
            color = get_color(func_name)
            func_name = colored(func_name, color)

        message = " ".join(str(arg) for arg in args)
        formatted_message = config["format_str"].format(
            func_name=func_name, message=message)

        if config["repeat_func_name"]:
            prefix, message = formatted_message.split(" ", 1)
            prefix += " "
            message = message.replace("\n", "\n" + prefix)
            formatted_message = prefix + message
        elif config["align"]:
            prefix, message = formatted_message.split(" ", 1)
            prefix += " "
            message = message.replace("\n", "\n" + " " * len(prefix))
            formatted_message = prefix + message

        kwargs['file'] = config["output"] or sys.stdout
        _original_print(formatted_message, **kwargs)


def get_color(func_name):
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    color_index = hash(func_name) % len(colors)
    return colors[color_index]


def activate():
    builtins.print = custom_print


def deactivate():
    builtins.print = _original_print
