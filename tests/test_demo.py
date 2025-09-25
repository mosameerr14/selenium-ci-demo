from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import pytest

@pytest.fixture
def driver():
    # Ensure a matching chromedriver is installed for your installed Chrome
    chromedriver_autoinstaller.install()  # installs or verifies chromedriver

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Let Selenium use the chromedriver installed by chromedriver_autoinstaller
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_example_dot_com_title(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title

def test_example_dot_com_heading(driver):
    driver.get("https://example.com")
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert h1.text.strip() == "Example Domain"
