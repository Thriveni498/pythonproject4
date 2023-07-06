import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pageobjects.loginpage import Login
from utilities.readproprties import ReadConfig
from utilities.CustomLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppliationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("---Test_001_Login--------")
        self.logger.info("-------started--------")
        # self.service_obj=Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "your store. Login":
            assert True
            self.driver.close()
            self.logger.info("-------home page test passed--------")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            assert False
            self.driver.close()

    def test_Login(self, setup):
        self.logger.info("-------verifying login test--------")
        # self.service_obj = Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.Setusername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        #self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("-------test login passed--------")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            assert False
            self.driver.close()
