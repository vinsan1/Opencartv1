from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():
    lnk_Myaccount_xpath="//span[normalize-space()='My Account']"
    lnk_regiser_linktext="Register"
    lnk_login_linktext="Login"

    def __init__(self,driver):
        self.driver=driver

    def ClickMyAcount(self):
        self.driver.find_element(By.XPATH,self.lnk_Myaccount_xpath).click()

    def Clickregister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_regiser_linktext).click()

    def Clicklogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()














