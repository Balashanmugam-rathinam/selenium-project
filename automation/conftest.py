import os
import pytest
from automation.utils.driver_setup import get_driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("automation/screenshots", exist_ok=True)
            driver.save_screenshot(f"automation/screenshots/{item.name}.png")

@pytest.fixture
def driver():
    driver = get_driver(headless=True)
    yield driver
    driver.quit()