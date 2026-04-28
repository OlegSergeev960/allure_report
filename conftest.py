import pytest
from selenium.webdriver import Chrome, ChromeOptions

@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def valid_credentials():
    return 'tomsmith', 'SuperSecretPassword!'

@pytest.fixture
def invalid_credentials():
    return 'tomsmit', 'SuperSecretPassword'