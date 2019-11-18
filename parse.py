import sys


KEYS_TO_FULL = {
    '-h': '--help',
    '-l': '--list',
    '-v': '--version'
}

KEYS = {
    '--help': 'Help',
    '--list': 'List',
    '--version': 'Version'
}


if __name__ == "__main__":
    for arg in sys.argv[1:]:

        arg, value = arg, None
        if '=' in arg:
            sep = arg.index('=')
            arg, value = arg[:sep], arg[sep + 1:]
        
        value_str = f' with value: {value}' if value is not None else ''

        if arg not in KEYS and arg not in KEYS_TO_FULL:
            print(f'Unknown Arg {arg.lstrip("-")}{value_str}')
            continue

        if arg not in KEYS:
            arg = KEYS_TO_FULL[arg]
        
        print(f'Arg {KEYS[arg]}{value_str}')
