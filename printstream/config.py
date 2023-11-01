_config = {
    "format_str": "[{func_name}] {message}",
    "level": 1,  # -1: none, 0: standard, 1: modified
    "output": None,  # None implies sys.stdout
    "align": True,
    "repeat_func_name": True,
    "colorize": True,
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


def get_config():
    return _config
