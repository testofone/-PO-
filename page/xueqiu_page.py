from appium import webdriver
from Appium_test.pageobjectTest.page.profile_page import ProfilePage
from Appium_test.pageobjectTest.page.search_page import SearchPage

class Xueqiu:
    def __init__(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": 'Hisense',
            "appActivity": ".view.WelcomeActivityAlias",
            "appPackage": "com.xueqiu.android",
            "unicodeKeybord": True,
            "resetKeybord": True,  # 方便在输入框中输入数据
            "autoGrantPermissions": True  # 这句代码会自动同意APP的权限请求
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(15)

    def goto_search(self):
        self.driver.find_element_by_id('tv_search').click()
        return SearchPage(self.driver)

