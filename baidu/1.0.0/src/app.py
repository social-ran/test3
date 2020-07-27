import asyncio
from walkoff_app_sdk.app_base import AppBase

class baidu(AppBase):
    __version__ = "1.0.0"
    app_name = "baidu"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def openweb(self, url, content):
        try:
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
        except:
            mystr = "no selenium"
            return mystr
        option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=/Users/apple/Library/Application Support/Google/Chrome/Default')
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=option)
        # browser=webdriver.Chrome()
        browser.get("http://www.baidu.com")
        browser.maximize_window()

        browser.find_element_by_id("kw").send_keys(content)
        browser.find_element_by_id("kw").send_keys(Keys.ENTER)
        return "OK!!"


if __name__ == "__main__":
    asyncio.run(baidu.run(), debug=True)
