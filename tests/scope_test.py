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
    r = s.get(FIRST_KEY)
    assert "-r" in r[0]
