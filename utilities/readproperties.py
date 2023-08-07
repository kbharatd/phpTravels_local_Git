import configparser

configuration = configparser.RawConfigParser()

configuration.read("C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site Practicing\\PhpTravel\\Configuration\\config.ini")

class Readconfig:

    @staticmethod
    def geturl():
        url = configuration.get('common info', 'Url')
        return url

    @staticmethod
    def getemail():
        email = configuration.get('common info', 'Email')
        return email

    @staticmethod
    def getpassword():
        password = configuration.get('common info', 'Password')
        return password
