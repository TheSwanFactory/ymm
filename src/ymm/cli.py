import re
import argparse
#import pkg_resources
from importlib.metadata import version
from pathlib import Path
from .keys import *
from .file import *
from .env import env

__version__ = version("ymm")

parser = argparse.ArgumentParser(description='Run actions.')
parser.add_argument('actions', metavar='action', nargs='*',default=DEFAULT_ACTION,
                    help='actions from <file> to execute')
parser.add_argument('-d','--debug', action='store_true',
                    help='print debugging information')
parser.add_argument('-f','--file', default=DEFAULT_FILE,
                    help='YAML file of actions')
parser.add_argument('-l','--list', action='store_true',
                    help='list available actions')
parser.add_argument('-n','--no-init', action='store_true',
                    help='skip init action')
parser.add_argument('-v','--version', action='version',
                    version=f'%(prog)s {__version__}')

def exec(ymm, args):
    keys = list(ymm.yaml.keys())
    if args.list:
        for key in keys: print(f' - {key}')
    ymm.env = env(args)
    actions = args.actions
    if (not args.no_init) & (INIT_ACTION in keys): ymm.run(INIT_ACTION)
    for action in actions:
        ymm.log(f'; {action}')
        results = ymm.run(action)
    return results

def main():
    args = parser.parse_args()
    #print(dir(args))
    ymm = load_file(args.file)
    return exec(ymm, args)

#main()
