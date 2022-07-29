from selenium import webdriver
from selenium.webdriver.common.by import By

class Registerpage():

    #Locators
    txtbox_firstname_id="input-firstname"
    txtbox_lastname_id="input-lastname"
    txtbox_email_id="input-email"
    txtbox_pwd_xpath="//input[@id='input-password']"
    chkbox_privacypolicy_xpath="//input[@name='agree']"
    btn_Continue_xpath="//button[@type='submit']"
    txt_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    # Constructors
    def __init__(self,driver):
        self.driver=driver

    #Action methods
    def setFirstName(self,username):
        self.driver.find_element(By.ID,self.txtbox_firstname_id).send_keys(username)

    def setlastname(self,lastname):
        self.driver.find_element(By.ID,self.txtbox_lastname_id).send_keys(lastname)

    def setemail(self,email):
        self.driver.find_element(By.ID,self.txtbox_email_id).send_keys(email)

    def setpwd(self,pwd):
        self.driver.find_element(By.XPATH,self.txtbox_pwd_xpath).send_keys(pwd)

    def clickprivacypolicy(self):
        self.driver.find_element(By.XPATH, self.chkbox_privacypolicy_xpath).click()

    def clickcontinue(self):
        self.driver.find_element(By.XPATH,self.btn_Continue_xpath).click()

    def getconfirmationmsg(self):
        try:
           return self.driver.find_element(By.XPATH,self.txt_msg_conf_xpath).text
        except:
            None







