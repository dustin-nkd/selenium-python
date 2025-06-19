import pytest
from framework.pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login("admin", "password")

    assert "Dashboard" in driver.title