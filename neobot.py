import os
try:
  from selenium import webdriver
except:
  os.system("pip install selenium")
  from selenium import webdriver
from time import sleep
from account import username, password
from xpaths import login_xpath, uname_xpath, passw_xpath, lsend_xpath, ads_xpath, adprize_xpath
from datetime import datetime
from datetime import timedelta

class NeoBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.neobux.com')
        sleep(1.5)
        log_btn = self.driver.find_element_by_xpath(login_xpath)
        log_btn.click()
        while not "m/l/?vl=" in self.driver.current_url:
          sleep(0.1)
        sleep(1.5)
        usern = self.driver.find_element_by_xpath(uname_xpath)
        usern.send_keys(username)
        passc = self.driver.find_element_by_xpath(passw_xpath)
        passc.send_keys(password)
        html = self.driver.page_source
        if "Código de Verificação" in html or "Verification Code" in html:  
          print("Waiting for human captcha to be solved... type the captcha then press enviar/send/login to login to proceed to automatic process")
        else:
          print("There's no captcha! proceding to automatically view the ads!")
          send_btn = self.driver.find_element_by_xpath(lsend_xpath)
          send_btn.click()
        while not "c/?vl=" in self.driver.current_url:
          sleep(0.1)
        sleep(1.5)

    def adclick(self):
        ads = self.driver.find_element_by_xpath(ads_xpath)
        ads.click()
        while not "m/v/?vl=" in self.driver.current_url:
          sleep(0.1)
        sleep(1.5)
        i = 1
        html = self.driver.page_source
        adc = 0
        finder = str(html).find("/v/?a=")
        if finder != -1:
          while True:
            finder = str(html).find("/v/?a=", finder)
            if finder == -1:
              break
            else:
              adc += 1
              finder += 1
  
          print('There are currently ' + str(adc) + ' ads available. it will take than ' + str(timedelta(seconds=int(adc) * 30)) + " or more to finish automatically view the ads")
          finder = 0
          startertimer = datetime.now()
          while True:  
            if i <= int(adc):
                ad = self.driver.find_element_by_xpath('//*[@id="l0l' + str(i) +'"]')
                ad.click()
                sleep(1)
                adr = self.driver.find_element_by_xpath('//*[@id="l' + str(i) +'"]')
                adr.click()
                i += 1
                sleep(28)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                print(str(round((i / (int(adc) + 1)) * 100)) + "%")
                sleep(1)
            else:
                break
          print("Finished in " + str(datetime.now() - startertimer) + "!")
        else:
          print("Ads not found for today")
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
    def done(self):
      self.driver.quit()

bot = NeoBot()
sleep(1)
bot.login()
bot.adclick()
sleep(10)
bot.done()
