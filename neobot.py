from selenium import webdriver
from time import sleep
from account import username, password
from xpaths import login_xpath, uname_xpath, passw_xpath, lsend_xpath, ads_xpath, total_xpath, adprize_xpath

class NeoBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.neobux.com')
        sleep(1)
        log_btn = self.driver.find_element_by_xpath(login_xpath)
        log_btn.click()
        sleep(1)
        usern = self.driver.find_element_by_xpath(uname_xpath)
        usern.send_keys(username)
        passc = self.driver.find_element_by_xpath(passw_xpath)
        passc.send_keys(password)
        send_btn = self.driver.find_element_by_xpath(lsend_xpath)
        send_btn.click()

    def adclick(self):
        ads = self.driver.find_element_by_xpath(ads_xpath)
        ads.click()
        sleep(2)

        i = 1
        adc = bot.driver.find_element_by_xpath(total_xpath).text

        print('There are currently ' + adc + ' ads available.')
        print(i)
        print(adc)
        sleep(2)
                            #
                            # Needs Improvement for Fixed Orange Advertisements
                            #
        while True:
            if i != int(adc):
                ad = self.driver.find_element_by_xpath('//*[@id="l0l' + str(i) +'"]')
                ad.click()
                adr = self.driver.find_element_by_xpath('//*[@id="l' + str(i) +'"]')
                adr.click()
                i += 1
                print(i)
                sleep(10)
            elif i == int(adc):
                break

    def adprize(self):
        i = 0
        adprize_text = self.driver.find_element_by_xpath(adprize_xpath).text
        while True:
            if i != int(adprize_text):
                self.driver.find_element_by_xpath(adprize_xpath).click()
                print('Waiting for the adPrize...' + str(i+1) + '/' + adprize_text)
                sleep(10)
                i += 1
                print('Done. Theres ' + str(int(adprize_text)-i) + ' adPrizes left.')
            elif i == int(adprize_text):
                print('Theres no adPrize left.')
                break

bot = NeoBot()
sleep(3)
bot.login()
sleep(3)

#bot.adclick()
#bot.adprize()
