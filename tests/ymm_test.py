#!/usr/bin/env python3
import pytest

@pytest.fixture
def ymm():
    return True

def test_load(ymm):
    assert ymm
