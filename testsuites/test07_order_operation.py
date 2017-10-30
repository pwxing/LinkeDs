# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_orderpage import OrderPage
import pageobjects


class OrderOperation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_order_operation001(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.login()
        time.sleep(2)
        # loginpage.get_windows_img()  # 调用基类截图方法
        # 点击电商按钮
        linkehomepage = LinkeHomePage(self.driver)
        time.sleep(1)
        linkehomepage.send_ds_link_btn()
        time.sleep(1)

        dshomepage = DSPage(self.driver)
        dshomepage.click_menu("订单管理")
        time.sleep(1)
        orderpage = OrderPage(self.driver)
        orderpage.click_menu("订单列表")
        time.sleep(1)
        # 输入时间
        orderpage.click_menu("全部订单")
        orderpage.click_menu("未付款")
        orderpage.click_menu("待审核")
        # orderpage.click_menu("201706100000038")

        # orderpage.click_query()
        # 输入到店门店，所属门店


        time.sleep(2)


if __name__ == '__main__':
    unittest.main()