import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("--language")
    print(f"\nЗапуск Chrome на языке: {lang}")

    options = Options()
    options.add_argument(f"--lang={lang}")
    options.add_experimental_option("prefs", {"intl.accept_languages": lang})

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()