import os
import sys
import ymm
from dataclasses import dataclass

TEST_FILE="tests/ymm.yml"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.','./src','..','../src')))

@dataclass
class Args:
    actions: list[str]
    file: str = TEST_FILE
    list: bool = False
    no_init: bool = False
