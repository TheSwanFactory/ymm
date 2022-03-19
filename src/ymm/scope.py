import os
from .keys import *
from .file import dict_file
from importlib.resources import path
MOD="ymm"

def env(args):
    ctx = dict(os.environ)
    for arg in vars(args):
        value = getattr(args, arg)
        ctx[arg] = getattr(args, arg)
    return ctx

class Scope:
    def __init__(self):
        self.scopes = []
        bpath = path(MOD, BUILTIN_FILE)
        builtin = dict_file(bpath)
        env = dict(os.environ)
        self.push(builtin)
        self.push(env)

    def push(self, ctx):
        self.scopes.append(ctx)
        return ctx

    def pop(self):
        ctx = self.scopes.pop()
        return ctx
