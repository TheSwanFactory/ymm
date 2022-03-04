DEFAULT_FILE="ymm.yml"

def from_file(yaml_file):
    print("Loading "+yaml_file)
    with open(yaml_file) as data:
        raw_yaml = yaml.full_load(data)
        return YMM(raw_yaml)

def run_file(yaml_file=DEFAULT_FILE):
    ymm = from_file(name, spark, folder)
    return ymm.run()
