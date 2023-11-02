_config = {
    "format_str": "[{func_name}] {message}",
    "level": 1,  # -1: none, 0: standard, 1: modified
    "output": None,  # None implies sys.stdout
    "align": True,
    "repeat_func_name": True,
    "colorize": True,
    "show_variables": False,
}


def set_format(format_str):
    _config["format_str"] = format_str


def set_level(level):
    _config["level"] = level


def set_output(output):
    _config["output"] = output


def set_align(align):
    _config["align"] = align


def set_repeat_func_name(repeat_func_name):
    _config["repeat_func_name"] = repeat_func_name


def set_colorize(colorize):
    _config["colorize"] = colorize

def set_show_variables(show_variables):
    _config["show_variables"] = show_variables


def get_config():
    return _config


def configure(format_str=None, level=None, output=None, align=None, repeat_func_name=None, colorize=None, show_variables=None):
    if format_str is not None:
        set_format(format_str)
    if level is not None:
        set_level(level)
    if output is not None:
        set_output(output)
    if align is not None:
        set_align(align)
    if repeat_func_name is not None:
        set_repeat_func_name(repeat_func_name)
    if colorize is not None:
        set_colorize(colorize)
    if set_show_variables is not None:
        set_show_variables(show_variables)
