#!/usr/bin/env python3
import pytest
from .context import *

@pytest.fixture
def y():
    return ymm.load_file(TEST_FILE)

def test_load(y):
    assert y
    assert y.env
    assert y.env.get(FIRST_KEY)

def test_run(y):
    result = y.run(FIRST_KEY)
    assert FIRST_KEY in result[0]
    key = f'{FIRST_KEY}#0'
    value = y.env.get(key)
    assert value

def test_dict(y):
    result = y.run("env")
    assert "value" in result[0]
    value = y.env.get("key")
    assert value
