from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

print(1)
chrome_options = webdriver.ChromeOptions()
print(2)
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")  # Replace with the correct port
print(3)
driver = webdriver.Chrome(options=chrome_options)
print(4)
# run in terminal for one constant chrome page with my log in:
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

time.sleep(3)
#elements = driver.find_elements(By.CSS_SELECTOR, "td[data-column-id='balance']")
#elements = driver.find_elements(By.CSS_SELECTOR, "td.column-balance.column-align-end")
elements = driver.find_elements(By.CSS_SELECTOR, "td.column-balance.column-align-end")
#elements = driver.find_elements(By.CSS_SELECTOR, "span.currency")
#elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'AED 0.50')]")

print(elements)
for i in elements:
    if i.text == 'AED 0.25':
        print(i)
        print(i.text)
        #time.sleep(5)
        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                i.click()
                y = True
            except:
                x += 0.5

        ##i.click()
        #time.sleep(3)
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
        ##edit_invoice = driver.find_element(By.CSS_SELECTOR, "div.StyledDrawer__FooterPrimaryAction-sc-1y21gq9-7.hUOBXj")
        #print(edit_invoice.text)
        #driver.execute_script("arguments[0].click();", edit_invoice)
        #edit_invoice = driver.find_element(By.XPATH, "//span[contains(text(), 'Edit invoice')]")

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                edit_invoice.click()
                y = True
            except:
                x += 0.5

        ##edit_invoice.click()
        #time.sleep(5)

        ##dropdown = element = driver.find_element(By.XPATH, "//*[text()='Discount percent']")
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

        ##dropdown.click()
        #time.sleep(3)
        ##disc_value = driver.find_element(By.XPATH, "//*[text()='Discount value']")

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                disc_value = driver.find_element(By.XPATH, "//*[text()='Discount value']")
                y = True
            except:
                x += 0.5


        #time.sleep(2)

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                disc_value.click()
                y = True
            except:
                x += 0.5

        ##disc_value.click()
        #time.sleep(3)

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                text_input = driver.find_element(By.CSS_SELECTOR, "input[data-automation-id='input-discount-sales']")
                y = True
            except:
                x += 0.5


        ##text_input = driver.find_element(By.CSS_SELECTOR, "input[data-automation-id='input-discount-sales']")

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

        ##save_button = driver.find_element(By.CSS_SELECTOR,"button[data-automation-id='btn-footer-save']")

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                save_button.click()
                y = True
            except:
                x += 0.5


        ##save_button.click()
        #time.sleep(3)

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                yes_button = driver.find_element(By.XPATH, '//button[text()="Yes"]')
                y = True
            except:
                x += 0.5

        ##yes_button = driver.find_element(By.XPATH, '//button[text()="Yes"]')

        x = 0
        y = False
        while y == False:
            try:
                time.sleep(x)
                yes_button.click()
                y = True
            except:
                x += 0.5


        ##yes_button.click()
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




        # Create an ActionChains object
        #action = ActionChains(driver)
        #action.move_to_element(element)
        #action.click()
        #action.perform()


driver.quit()

#driver = webdriver.Chrome()
#driver.get('https://app.qbo.intuit.com/app/invoices')

#elements = driver.find_elements(By.CSS_SELECTOR, 'td.column-balance[data-column-id="balance"]')

#print(elements)
'''
element = driver.find_element_by_id('element_id')
action = ActionChains(driver)
action.move_to_element(element).perform()


element = driver.find_element_by_id('element_id')
action = ActionChains(driver)
action.click(element).perform()
'''
