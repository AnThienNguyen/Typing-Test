from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
browser.get('https://10fastfingers.com/advanced-typing-test/english')

word = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='highlight']")))
inputBox = browser.find_element_by_xpath("//input[@id='inputfield']")
wordFound = True

while wordFound:
    if (len(browser.find_elements_by_xpath("//span[@class='highlight']"))) > 0:
        text = browser.find_element_by_xpath("//span[@class='highlight']").text
        print(text)
        inputBox.send_keys(text)
        time.sleep(.100)
        inputBox.send_keys(" ")
        time.sleep(.100)

        if (len(browser.find_elements_by_xpath("//div[@id='auswertung-result']/h3"))) > 0:
            wordFound = False
    else:
        print("No more words found")
        wordFound = False

time.sleep(2)
browser.find_element_by_xpath("//div[@id='auswertung-result']").screenshot('images/results.png')

browser.quit()