#!/usr/bin/env python3
import pytest
from .context import *

@pytest.fixture
def y():
    print(dir(ymm))
    return ymm.load_file(TEST_FILE)

def test_load(y):
    assert y
    assert y.yaml
