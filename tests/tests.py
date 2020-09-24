from selenium import webdriver
from holmium.core import Page, Element, Locators, TestCase
from pageobjects.form import SauceDemoTest
from nose.tools import assert_true, assert_false, assert_equal
import data_layer as data
import time
import nose

class SauceDemoPageTest(TestCase):
    def setUp(self):
        
        #Please provide chrome driver path explicitly here 
        self.driver = webdriver.Chrome("D:\chromedriver.exe") 
        self.url = "https://www.saucedemo.com"
        self.username = data.USER_NAME
        self.password =  data.PASSWORD
        self.page = SauceDemoTest(self.driver, self.url)
        self.page.user_name_input.send_keys(data.USER_NAME)
        self.page.password_input.send_keys(data.PASSWORD)
        self.page.login_button.click()

    def test_login(self):
        """
        Validate user able to login
        """

        assert_true(self.page.product_label)
        assert_equal(self.page.product_label.text, data.PRODUCT_LABEL)

    def test_product_info(self):
        """
        Verify user able to check product info
        """
        assert_true(self.page.product_list)
        product_label = self.page.product_list[0].text
        self.page.product_list[0].click()
        assert_true(self.page.product_info_label)
        assert_equal(product_label,self.page.product_info_label.text)

    def test_adding_product_to_cart(self):
        """
        verify user able add product to the cart and remove
        """
        assert_true(self.page.product_cart_list)
        product_name = self.page.product_list[0].text
        self.page.product_cart_list[0].click()
        self.page.cart.click()
        cart_product_name = self.page.cart_items[0].text
        assert_equal(product_name, cart_product_name)
        self.page.remote_items[0].click()
        assert_false(self.page.cart_items)   


    def tearDown(self):
        self.page.menu_button.click()
        self.page.logout_user.click()
        self.driver.close()