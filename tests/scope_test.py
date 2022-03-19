#!/usr/bin/env python3
import pytest
from .context import *

@pytest.fixture
def s():
    ctx = ymm.Scope()
    return ctx

def test_scope(s):
    print(dir(s))
    assert s

def test_builtin(s):
    #s.get()
    print(dir(s))
    assert s
