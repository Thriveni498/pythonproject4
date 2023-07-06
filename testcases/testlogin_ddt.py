
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageobjects.loginpage import Login
from utilities.readproprties import ReadConfig
from utilities.CustomLogger import LogGen
from utilities import XLUtils

class Test_002_Login:
    path =".\\TestData\mytestdata.xlsx"
    baseURL = ReadConfig.getAppliationURL()
    # username = ReadConfig.getusername()
    # password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    # def test_homepageTitle(self, setup):
    #     self.logger.info("---Test_001_Login--------")
    #     self.logger.info("-------started--------")
    #     # self.service_obj=Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     # self.driver.close()
    #     if act_title == "your store. Login":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("-------home page test passed--------")
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
    #         assert False
    #         self.driver.close()

    def test_Login_ddt(self, setup):
        self.logger.info("-------verifying login test--------")
        # self.service_obj = Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rows =XLUtils.getRow(self.path ,'Sheet1')
        print("Number of rows is:" ,self.rows)
        self.columns = XLUtils.getcolumn(self.path, 'Sheet1')
        print("Number of columns is:" ,self.columns)
        lst_status = []
        self.lp = Login(self.driver)
        for r in range(2 ,self.rows):
            self.username =XLUtils.readdata(self.path ,'Sheet1' ,r ,1)
            self.password = XLUtils.readdata(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readdata(self.path, 'Sheet1', r, 3)
            self.lp.Setusername(self.username)
            self.lp.Setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp=='pass':
                    self.logger.info("***passed****")
                    self.lp.clicklogout()
                    lst_status.append('pass')
                elif self.exp=='fail':
                    self.logger.info("***passed****")
                    self.lp.clicklogout()
                    lst_status.append('fail')
            elif act_title != exp_title:
                if self.exp=='pass':
                    self.logger.info("***passed****")
                    #self.lp.clicklogout()
                    lst_status.append('fail')
                elif self.exp=='fail':
                    self.logger.info("***passed****")
                    #self.lp.clicklogout()
                    lst_status.append('pass')
        if 'fail' not in lst_status:
            print("login test passed")
            self.driver.close()
            assert True
        else:
            print("login test failed")
            self.driver.close()
            assert False
