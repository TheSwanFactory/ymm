import os
from .keys import *
from importlib.resources import read_text

def env(args):
    ctx = dict(os.environ)
    for arg in vars(args):
        value = getattr(args, arg)
        ctx[arg] = getattr(args, arg)
    return ctx
