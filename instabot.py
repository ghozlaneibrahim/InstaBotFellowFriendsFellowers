from selenium import webdriver
from time import sleep
import selenium

browser = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\chromedriver.exe")
browser.get("https://www.instagram.com")
sleep(4)

# Select the driver, In our case we will use Chrome.

username_input = str(input('username :'))
password_input = str(input('password :'))

username = browser.find_elements_by_xpath("//input[@name=\"username\"]")[0]
username.send_keys(username_input)
password = browser.find_elements_by_xpath("//input[@name=\"password\"]")[0]
password.send_keys(password_input)
log_in = browser.find_elements_by_xpath('//button[@type="submit"]')[0]
log_in.click()
sleep(4)
try:
    browser.find_elements_by_xpath("//button[contains(text(),'not now')]").click()
except:
    instagram_link = input('type the link of your friend  you are want to fellow his fellowers')
    browser.get(instagram_link)

log_in = browser.find_elements_by_xpath('//a[contains(@href,"/followers")]')[0]

log_in.click()
sleep(5)
# log_in = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')[0]
# log_in.click()
i = 1
while True:
    try:

        log_in = \
            browser.find_elements_by_xpath(
                '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(i))[
                0]
        verif=browser.find_elements_by_xpath("//div[contains(@href,'/YourInstaAccount')]")[0]  # your instagram account

        "/html/body/div[4]/div/div/div[2]/ul/div/li[29]/div/div[2]/button"
        "/html/body/div[4]/div/div/div[2]/ul/div/li[26]/div/div[2]/button"



        log_in.click()




        i += 1

        sleep(1)
    except selenium.common.exceptions.ElementClickInterceptedException:
        log_in = browser.find_elements_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")[0]

        log_in.click()

        i += 1
    except IndexError:
        break
