import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Attach driver context to the running test session for screenshots
    if request.node:
        request.node.funcargs['driver'] = driver

    yield driver
    driver.quit()


# Hook logic to watch tests and save visual assets on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Create screenshots directory structure dynamically
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Save standard PNG format asset
            clean_name = item.name.replace("[", "_").replace("]", "_")
            screenshot_path = os.path.join(screenshot_dir, f"{clean_name}.png")
            driver.save_screenshot(screenshot_path)

            # Embed preview asset linking cleanly directly into HTML outputs
            if hasattr(report, "extra"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    html_path = os.path.relpath(screenshot_path, os.path.dirname(__file__))
                    extra = pytest_html.extras.html(f'<img src="{html_path}" style="width:304px;height:228px;" '
                                                    f'action="click" target="_blank" align="right"/>')
                    report.extra.append(extra)
