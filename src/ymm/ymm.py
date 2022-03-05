import subprocess

class YMM:
    def __init__(self, yaml, debug=True):
        self.yaml = yaml
        self.env = {}

    def run(self,arg=False):
        actions = self.yaml[arg]
        results = [self.execute(cmd) for cmd in actions]
        return results

    def execute(self, cmd):
        args = cmd.split(" ")
        self.log(args)
        result = subprocess.run(args, stdout=subprocess.PIPE)
        msg = result.stdout.decode("utf-8")
        self.log(f'# {msg}')
        return msg.strip()

    def log(self, arg):
        if self.env['debug']: print(f'YMM.log {arg}')
