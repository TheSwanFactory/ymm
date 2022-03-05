import argparse
from .file import *

parser = argparse.ArgumentParser(description='Run actions.')
parser.add_argument('actions', metavar='action', nargs='+',
                    help='actions from ymm.yaml to execute')
parser.add_argument('-f','--file', default=DEFAULT_FILE,
                    help='YAML file of actions')
parser.add_argument('-d','--debug', action='store_true',
                    help='print debugging information')
def main():
    args = parser.parse_args()
    actions = args.actions
    file = args.file
    ymm = load_file(file)
    ymm.debug = args.debug
    for action in actions:
        ymm.log(f'; {action}')
        results = ymm.run(action)

#main()
