import yaml
import os,shutil
from .keys import DEFAULT_FILE
from .ymm import YMM

def dict_file(yaml_file):
    print(f"Loading {yaml_file}")
    with open(yaml_file) as data:
        raw_yaml = yaml.full_load(data)
        return raw_yaml
