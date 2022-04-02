import os
import json
from .keys import *
from .file import dict_file
from importlib.resources import path

class Scope:
    def __init__(self):
        self.scopes = []
        bpath = path(MOD, BUILTIN_FILE)
        builtin = dict_file(bpath)
        env = dict(os.environ)
        self.push(".builtin", builtin)
        self.push(".env", env)

    def args(self, args):
        ctx = {k: getattr(args, k) for k in vars(args)}
        return self.push('.args', ctx)

    def push(self, name, ctx = {}):
        ctx[kID] = name
        self.scopes.append(ctx)
        return ctx

    def pop(self):
        ctx = self.scopes.pop()
        return ctx

    def get(self, key, default=None):
        for ctx in reversed(self.scopes):
            if key in ctx: return ctx[key]
        return default

    def set(self, key, value):
        ctx = self.scopes[-1]
        ctx[key] = value
        return value

    def flat(self):
        values = {k: v for d in self.scopes for k, v in d.items()}
        return values

    def flatstr(self):
        jvals = {k: fixup(v) for k, v in self.flat().items()}
        return jvals

    def actions(self):
        dict = self.flat();
        actions = [k for k,v in dict.items() if not isinstance(v, str)]
        return actions

def fixup(v):
    s = json.dumps(v)
    return s.replace(': ',':')
