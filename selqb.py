from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

# run in terminal for static chrome page with my log in:
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")  # Replace with the correct port
driver = webdriver.Chrome(options=chrome_options)

elements = driver.find_elements(By.CSS_SELECTOR, "td.column-balance.column-align-end")

for i in elements:
    if i.text == 'AED 0.25':
        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                i.click()
                y = True
            except:
                x += 0.5

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                edit_invoice = driver.find_element(By.CSS_SELECTOR,
                                                   "div.StyledDrawer__FooterPrimaryAction-sc-1y21gq9-7.hUOBXj")
                y = True
            except:
                x += 0.5


        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                edit_invoice.click()
                y = True
            except:
                x += 0.5


        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                dropdown = element = driver.find_element(By.XPATH, "//*[text()='Discount percent']")
                y = True
            except:
                x += 0.5

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                dropdown.click()
                y = True
            except:
                x += 0.5

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                disc_value = driver.find_element(By.XPATH, "//*[text()='Discount value']")
                y = True
            except:
                x += 0.5


        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                disc_value.click()
                y = True
            except:
                x += 0.5
        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                text_input = driver.find_element(By.CSS_SELECTOR, "input[data-automation-id='input-discount-sales']")
                y = True
            except:
                x += 0.5


        time.sleep(2)
        text_input.send_keys(".24")
        time.sleep(2)

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                save_button = driver.find_element(By.CSS_SELECTOR,"button[data-automation-id='btn-footer-save']")
                y = True
            except:
                x += 0.5

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                save_button.click()
                y = True
            except:
                x += 0.5


        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                yes_button = driver.find_element(By.XPATH, '//button[text()="Yes"]')
                y = True
            except:
                x += 0.5

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                yes_button.click()
                y = True
            except:
                x += 0.5

        time.sleep(3)


        try:
            yes_button2 = driver.find_element(By.XPATH, '//button[text()="Yes"]')
            yes_button2.click()
            time.sleep(3)
            close_button = driver.find_element(By.CSS_SELECTOR, 'i.hi-close')
            close_button.click()
        except:
            close_button = driver.find_element(By.CSS_SELECTOR, 'i.hi-close')
            close_button.click()
            time.sleep(3)

driver.quit()



