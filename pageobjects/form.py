from holmium.core import Page, Element, Elements, ElementMap, Locators, conditions
from pageobjects import form_pageobjects

class SauceDemoTest(Page):
    """
    This class is use for defining all the page source objects.
    Args : Page
    """
    user_name_input = Element(Locators.ID, form_pageobjects.USER_NAME, only_if=conditions.VISIBLE(), timeout=60)
    password_input = Element(Locators.ID, form_pageobjects.PASSWORD, only_if=conditions.VISIBLE(), timeout=60)
    login_button = Element(Locators.ID, form_pageobjects.LOGIN_BUTTON, only_if=conditions.VISIBLE(), timeout=60)
    product_label = Element(Locators.CSS_SELECTOR, form_pageobjects.PRODUCT_LABEL, only_if=conditions.VISIBLE(), timeout=60)
    product_list = Elements(Locators.CSS_SELECTOR, form_pageobjects.PRODUCTS_LIST, only_if= lambda el :el[0].is_displayed(), timeout=60)
    product_info_label = Element(Locators.CSS_SELECTOR, form_pageobjects.PRODUCT_INFO_LABEL, only_if=conditions.VISIBLE(), timeout=60)
    product_cart_list = Elements(Locators.CSS_SELECTOR, form_pageobjects.PRODUCT_CART_LIST, only_if= lambda el :el[0].is_displayed(), timeout=60)
    cart = Element(Locators.CSS_SELECTOR, form_pageobjects.CART, only_if=conditions.VISIBLE(), timeout=60)
    cart_items = Elements(Locators.CSS_SELECTOR, form_pageobjects.CART_ITEMS, only_if= lambda el :el[0].is_displayed(), timeout=60)
    remote_items = Elements(Locators.CSS_SELECTOR, form_pageobjects.REMOVE_ITEMS, only_if= lambda el :el[0].is_displayed(), timeout=60)
    menu_button = Element(Locators.CSS_SELECTOR, form_pageobjects.MENU, only_if=conditions.VISIBLE(), timeout=60)
    logout_user = Element(Locators.ID, form_pageobjects.LOGOUT, only_if=conditions.VISIBLE(), timeout=60)
