import time

from pageObject.Login import LoginPage
from utilities.readproperties import Readconfig
from utilities.Logger import LogGenerator


class Test_Login:
    Url = Readconfig.geturl()
    Email = Readconfig.getemail()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_page_title_001(self, setup):
        self.log.info("test_page_title_001 is started")

        self.driver = setup
        self.log.info("Opening Browser")

        self.lp = LoginPage(self.driver)

        self.driver.get(self.Url)
        self.log.info("Go to this url--->" + self.Url)

        if self.driver.title == "Administrators Login":
            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site "
                "Practicing\\PhpTravel\\Screenshots\\test_page_title_001_passed.png")
            assert True
            print("test_page_title_001 is passed")
            self.log.info("test_page_title_001 is passed")
        else:
            print("test_page_title_001 is failed")
            self.log.info("test_page_title_001 is passed")

            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site "
                "Practicing\\PhpTravel\\Screenshots\\test_page_title_001_Failed.png")

            assert False

        print("test_test_page_title_001 is completed")
        self.log.info("test_test_page_title_001 is completed")

    def test_login_002(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")

        self.lp = LoginPage(self.driver)
        self.driver.get(self.Url)
        self.log.info("Go to this url--->" + self.Url)

        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Email--->" + self.Email)

        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password--->" + self.Password)

        self.lp.Click_Login()
        self.log.info("Click on login")

        time.sleep(5)

        if self.driver.title == "Dashboard":

            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site "
                "Practicing\\PhpTravel\\Screenshots\\test_login_002_passed.png")

            time.sleep(4)
            self.lp.Click_Menu()
            self.log.info("Click on Menu")

            time.sleep(2)
            self.lp.Click_Logout()
            self.log.info("Click on logout")

            assert True
            self.driver.close()
            print("test_login_002 is passed")
            self.log.info("test_login_002 is passed")

        else:
            print("test_login_002 is failed")
            self.log.info("test_login_002 is failed")

            self.driver.save_screenshot(
                "C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site "
                "Practicing\\PhpTravel\\Screenshots\\test_login_002_failed.png")

            assert False

        print("test_login_002 is completed")
        self.log.info("test_login_002 is completed")
