import subprocess
import sys
from .keys import *

class YMM:
    def __init__(self, yaml, debug=True):
        self.yaml = yaml
        self.env = {}
        self.i = 0

    def run(self,arg=False):
        if not arg in self.yaml: sys.exit(f'ERROR: action [{arg}] not found')
        actions = self.yaml[arg]
        self.i = 0
        self.arg = arg
        results = [self.execute(cmd) for cmd in actions]
        return results

    def execute(self, cmd):
        if cmd[0] == kCall: return "\n".join(self.run(cmd[1:]))
        sub = cmd.format(**self.env)
        args = sub.split(" ")
        self.log(args)
        result = subprocess.run(args, stdout=subprocess.PIPE)
        msg = result.stdout.decode("utf-8").strip()
        self.save(msg)
        return msg

    def save(self, msg):
        print(f'# {msg}')
        self.i += 1
        key = f'{self.arg}.{self.i}'
        if kLast in self.env: self.env[kPrior] = self.env[kLast]
        self.env[kLast]=msg
        self.env[key]=msg
        return msg

    def log(self, arg):
        if self.env.get(kLog, False): print(f'YMM.log {arg}')
