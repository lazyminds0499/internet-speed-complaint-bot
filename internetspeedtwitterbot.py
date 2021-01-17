from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


TWITTER_USERNAME = "NitinYa64709470"
TWITTER_PASSWORD = "7988nky@#0"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_drive_path = "C:/Users/Nitin/Development/chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=self.chrome_drive_path, options=self.options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                      'div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(45)
        download_speed = self.driver.find_element_by_css_selector(".result-item-download .u-align-left span")
        upload_speed = self.driver.find_element_by_css_selector(".result-item-upload .u-align-left span")
        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)

    def tweet_at_provider(self, down, up):
        self.driver.get(url="https://twitter.com/home")
        time.sleep(5)
        inputs = self.driver.find_elements_by_css_selector(".css-1dbjc4n .css-1dbjc4n .css-901oao input")
        user_name_input = inputs[0]
        user_name_input.send_keys(TWITTER_USERNAME)
        password_input = inputs[1]
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/'
                                                  'div/div/div[1]/div[3]/a')
        tweet.click()
        time.sleep(2)
        to_write = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                                     'div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/'
                                                     'div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        to_write.send_keys(f"Hello internet provider. Why is my internet speed {self.down}down/{self.up}up. when"
                           f" i pay for {down}down/{up}up. ")
        time.sleep(3)
        final_tweet = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                        'div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]'
                                                        '/div/div/div[2]/div[4]/div/span/span')
        final_tweet.click()