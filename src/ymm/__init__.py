# ymm v0.1
# YAML Mimics Makefiles

DEFAULT_FILE="ymm.yml"

class YMM:
    def __init__(self, yaml):
        self.yaml = yaml

    def run(self):
        return True

def from_file(yaml_file):
    print("Loading "+yaml_file)
    with open(yaml_file) as data:
        raw_yaml = yaml.full_load(data)
        return YMM(raw_yaml)

def run_file(yaml_file=DEFAULT_FILE):
    ymm = from_file(name, spark, folder)
    return ymm.run()
