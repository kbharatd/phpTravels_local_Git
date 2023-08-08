import time

import pytest

from pageObject.Login import LoginPage
from utilities import XLutils
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login_DDT:
    Url = Readconfig.geturl()
    Email = Readconfig.getemail()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site " \
           "Practicing\\PhpTravel\\testCases\\TestData\\LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt_004(self, setup):
        self.driver = setup
        time.sleep(3)
        self.log.info("Opening Browser")

        self.lp = LoginPage(self.driver)
        self.driver.get(self.Url)
        self.log.info("Go to this url--->" + self.Url)

        time.sleep(3)

        self.rows = XLutils.getrowCount(self.path, "Sheet1")
        print("Number Rows--->", self.rows)

        status_list = []
        for r in range(2, self.rows + 1):

            self.Email_Id = XLutils.getreaddData(self.path, "Sheet1", r, 2)
            self.Password_Id = XLutils.getreaddData(self.path, "Sheet1", r, 3)
            self.Expt_result = XLutils.getreaddData(self.path, "Sheet1", r, 4)

            self.lp.Enter_Email(self.Email_Id)
            self.log.info("Entering Email--->" + self.Email_Id)

            self.lp.Enter_Password(self.Password_Id)
            self.log.info("Entering Password--->" + self.Password_Id)

            time.sleep(3)

            self.lp.Click_Login()
            self.log.info("Click on login")

            time.sleep(5)
            if self.driver.title == "Dashboard":
                if self.Expt_result == "Pass":

                    self.log.info("Page Title -->" + self.driver.title)

                    self.lp.Click_Menu()
                    self.log.info("Clicking Menu Button")

                    self.driver.save_screenshot(
                        "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site "
                        "Practicing\\PhpTravel\\Screenshots\\test_login_002_passed.png")

                    # time.sleep(2)

                    self.lp.Click_Logout()
                    self.log.info("Clicking Logout Button")

                    status_list.append("Pass")
                    XLutils.getwriteData(self.path, "Sheet1", r, 5, "Pass")

                elif self.Expt_result == "Fail":

                    self.log.info("Page Title -->" + self.driver.title)

                    self.lp.Click_Menu()
                    self.log.info("Clicking Menu Button")

                    self.driver.save_screenshot(
                        "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site "
                        "Practicing\\PhpTravel\\Screenshots\\test_login_002_failed.png")

                    # time.sleep(2)

                    self.lp.Click_Logout()
                    self.log.info("Clicking Logout Button")

                    status_list.append("Fail")
                    XLutils.getwriteData(self.path, "Sheet1", r, 5, "Fail")

            else:
                if self.Expt_result == "Pass":

                    self.log.info("Page Title -->" + self.driver.title)

                    # self.driver.save_screenshot(
                    #     "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
                    #     "\\" + self.Email + self.Password + "test_login_Params_003_fail.PNG")

                    status_list.append("Fail")
                    XLutils.getwriteData(self.path, "Sheet1", r, 5, "Fail")

                elif self.Expt_result == "Fail":

                    self.log.info("Page Title -->" + self.driver.title)

                    # self.driver.save_screenshot(
                    #     "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel\\Screenshots"
                    #     "\\" + self.Email + self.Password + "test_login_Params_003_pass.PNG")

                    status_list.append("Pass")

                    XLutils.getwriteData(self.path, "Sheet1", r, 5, "Pass")

        time.sleep(2)
        print(status_list)
        if "Fail" not in status_list:
            self.log.info("test_login_ddt_004 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_004 is Failed")
            assert False

        print("test_login_ddt_004 is completed")
        self.log.info("test_login_ddt_004 is completed")
