import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from walkoff_app_sdk.app_base import AppBase

class baidu(AppBase):
    __version__ = "1.0.0"
    app_name = "baidu"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def openweb(self, url, content):
        option = webdriver.ChromeOptions()
        option.add_argument('--user-data-dir=/Users/apple/Library/Application Support/Google/Chrome/Default')
        browser = webdriver.Chrome(chrome_options=option)
        browser.get(url)
        browser.maximize_window()

        browser.find_element_by_id("kw").send_keys(content)
        browser.find_element_by_id("kw").send_keys(Keys.ENTER)
        return "OK!!"


if __name__ == "__main__":
    asyncio.run(baidu.run(), debug=True)
