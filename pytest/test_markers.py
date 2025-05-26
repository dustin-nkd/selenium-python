# test_markers.py

import pytest

@pytest.mark.smoke
def test_login():
    print("Running Smoke Test: test_login")
    assert True

@pytest.mark.regression
def test_add_item_to_cart():
    print("Running Regression Test: test_add_item_to_cart")
    assert True

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout():
    print("Running Smoke + Regression Test: test_checkout")
    assert True

def test_no_marker():
    print("Running test with no marker")
    assert True