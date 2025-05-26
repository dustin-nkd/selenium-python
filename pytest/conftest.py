# conftest.py

import pytest

# Example 1: A simple fixture that returns a number
@pytest.fixture
def sample_number():
    print("\nSetting up sample_number fixture")
    return 42

# Example 2: A fixture that provides a list
@pytest.fixture
def sample_list():
    print("\nSetting up sample_list fixture")
    return ["apple", "banana", "cherry"]

# Example 3: A fixture with setup and teardown using yield
@pytest.fixture() # auto apply this fixture to test method autouse=True, scope="class"
def setup_and_teardown():
    print("\n[Setup] Open resource (e.g., DB connection, browser)")
    resource = "Resource Ready"
    yield resource
    print("\n[Teardown] Clean up resource (e.g., close connection, quit browser)")