from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
 
AUTH = 'brd-customer-hl_29454674-zone-ai_scraper:jtrzxe76kv15'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
def scrape_website(website):
    """"""
    print("Lunching chrome browser...")

    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html


