from browserstack.local import Local
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

USERNAME = ""
ACCESS_KEY = ""

bstack_options = {
    "os": "windows",
    "osVersion": "10",
    "buildName": "generic_Timeout-Win10",
    "sessionName": "DemoSession",
    "userName": USERNAME,
    "accessKey": ACCESS_KEY,
    "debug": "true",
    "networkLogs": "true",
    "idleTimeout": 300,
    "local": "true"
}
bs_local_args = {"key": ACCESS_KEY}


# Initialize BrowserStack Local and WebDriver options
options = ChromeOptions()
tool_options = "bstack:options", bstack_options
options.browser_version = "latest"
options.set_capability(tool_options[0], tool_options[1])

# Start the BrowserStack Local connection
BS_LOCAL_URL = Local()
BS_LOCAL_URL.start(**bs_local_args)

driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub", 
    options=options
)

# Implicit wait is applied here
driver.implicitly_wait(30)

try:
    driver.get("https://google.com")
    # Wait for the search bar element to be visible
    WebDriverWait(driver, 30).until(
        ec.visibility_of_element_located((By.XPATH, "//textarea[@id='APjFq']"))
    )
finally:
    driver.quit()  # Quit the driver after each loop iteration
    BS_LOCAL_URL.stop()  # Stop the local connection

    