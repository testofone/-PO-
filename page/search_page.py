from appium.webdriver.webdriver import WebDriver


class SearchPage:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def search(self,keywords):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keywords)
        self.driver.press_keycode(66)
        self.driver.find_element_by_id('name').click()
        return self

    def get_befor_txt(self,index):
        return self.driver.find_elements_by_id('follow_btn')[index]

    def get_after_txt(self):
        return self.driver.find_element_by_id('followed_btn')