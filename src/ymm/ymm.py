import subprocess
import sys
from .keys import *
from .scope import Scope

def is_dict(d): return isinstance(d, dict)

def shell(args):
    result = subprocess.run(args, stdout=subprocess.PIPE)
    msg = result.stdout.decode("utf-8").strip()
    return msg

class YMM:
    def __init__(self, yaml):
        self.env = Scope()
        self.env.push("ymm", yaml)
        self.actions = self.env.actions()
        self.printOutput = True

    def run(self,action=DEFAULT_ACTION, hide=True):
        currentOutput = self.printOutput
        if hide: self.printOutput = False
        if not action in self.actions:
            msg = f'ERROR: action [{action}] not found' if action != DEFAULT_ACTION else "Exiting"
            sys.exit(msg)
        self.env.push(action)
        cmds = self.env.get(action)
        cdict = cmds if is_dict(cmds) else {f'{action}#{i}': cmd for i,cmd in enumerate(cmds)}
        results = [self.execute(v, k) for k,v in cdict.items()]
        if hide: self.printOutput = currentOutput
        return results

    def execute(self, cmd, key):
        self.log(f'! {key}: {cmd}', "execute")
        if not isinstance(cmd,str): return self.save(cmd, key)
        variables = self.env.flatstr()
        text = cmd.format(**variables)
        args = text.split(" ")
        self.log(args, "commands")
        sigil = args.pop(0)
        if sigil == kCall: return "\n".join(self.run(args[0])) # run named action
        if sigil == kShell: text = shell(args)
        if text and isinstance(text,str): return self.save(text, key)
        return text

    def save(self, msg, key):
        if self.printOutput: print(f'# {key}: {msg}')
        #if kLast in self.env: self.env[kPrior] = self.env[kLast]
        self.env.set(kLast, msg)
        self.env.set(key, msg)
        return msg

    def log(self, event, caption=False):
        if self.env.get(kLog, False):
            prefix = f'DEBUG_{caption}' if caption else 'DEBUG'
            print(f'{prefix} {event}')
