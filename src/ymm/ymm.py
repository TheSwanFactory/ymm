import subprocess

def execute(cmd):
        args = cmd.split(" ")
        print(args)
        result = subprocess.run(args, stdout=subprocess.PIPE)
        msg = result.stdout.decode("utf-8")
        return msg.strip()


class YMM:
    def __init__(self, yaml):
        self.yaml = yaml

    def run(self,arg=False):
        actions = self.yaml[arg]
        results = [execute(cmd) for cmd in actions]
        return results
