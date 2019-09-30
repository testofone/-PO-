from Appium_test.pageobjectTest.page.xueqiu_page import Xueqiu

page = Xueqiu()
icon_text = page.goto_search().search('zhaoshangyinhang')
icon_text.get_befor_txt(0).click()
assert icon_text.get_after_txt().get_attribute('text') =='已添加'

icon_text.get_after_txt().click()
assert icon_text.get_befor_txt(0).get_attribute('text') =='加自选'