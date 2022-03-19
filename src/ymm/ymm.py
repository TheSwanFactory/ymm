import subprocess
import sys
from .keys import *
from .scope import Scope

class YMM:
    def __init__(self, yaml):
        self.yaml = yaml
        self.env = Scope()
        self.i = 0

    def actions(self):
        return list(self.yaml.keys())

    def run(self,action=DEFAULT_ACTION):
        if not action in self.yaml:
            msg = f'ERROR: action [{action}] not found' if action != DEFAULT_ACTION else "Exiting"
            sys.exit(msg)
        self.env.push(action)
        commands = self.yaml[action]
        self.action = action
        self.i = 0
        results = [self.execute(cmd) for cmd in commands]
        self.env.pop()
        return results

    def execute(self, cmd):
        if cmd[0] == kCall: return "\n".join(self.run(cmd[1:]))
        sub = cmd.format(**self.env.flat())
        commands = sub.split(" ")
        self.log(commands)
        result = subprocess.run(commands, stdout=subprocess.PIPE)
        msg = result.stdout.decode("utf-8").strip()
        self.save(msg)
        return msg

    def save(self, msg):
        self.i += 1
        key = f'{self.action}#{self.i}'
        print(f'  {key}: {msg}')

        #if kLast in self.env: self.env[kPrior] = self.env[kLast]
        self.env.set(kLast, msg)
        self.env.set(key, msg)
        return msg

    def log(self, action):
        if self.env.get(kLog, False): print(f'YMM.log {action}')
