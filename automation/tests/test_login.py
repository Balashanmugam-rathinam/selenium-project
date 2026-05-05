import pytest

@pytest.mark.parametrize("username,password,expected", [
    ("admin", "123456", "Dashboard"),
    ("wrong", "wrong", "Invalid"),
])
def test_login_variants(driver, username, password, expected):
    from automation.pages.login_page import LoginPage
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    if expected == "Dashboard":
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "logout-btn"))
        )
        assert "Dashboard" in driver.title
    else:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        assert "Invalid" in driver.find_element(By.ID, "message").text