import os
from .keys import *
from .file import dict_file
from importlib.resources import path

class Scope:
    def __init__(self):
        self.scopes = []
        bpath = path(MOD, BUILTIN_FILE)
        builtin = dict_file(bpath)
        env = dict(os.environ)
        self.push(builtin, "builtin")
        self.push(env, "env")

    def push(self, ctx, name=None):
        ctx[kID] = name if name else str(len(self.scopes))
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
