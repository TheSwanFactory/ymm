from .keys import *

def context(args):
    ctx = dict(os.environ)
    for arg in vars(args):
        value = getattr(args, arg)
        ctx[arg] = getattr(args, arg)
    return ctx
