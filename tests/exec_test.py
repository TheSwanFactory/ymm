#!/usr/bin/env python3
import pytest
from .context import *

FIRST_KEY='install'

@pytest.fixture
def y():
    return ymm.load_file(TEST_FILE)

def yexec(y, s):
    args = Args([s])
    result = ymm.exec(y,args)
    return result

def test_exec(y):
    result = yexec(y, 'install')
    assert FIRST_KEY in result[0]

def test_shell(y):
    s = "$ ls"
    result = y.execute(s, "shell")
    assert "test" in result
    result = yexec(y, 'echo')
    assert '"A":"B"' in result[0]

def test_call(y):
    result = yexec(y, 'call')
    assert '"A":"B"' in result[0]
