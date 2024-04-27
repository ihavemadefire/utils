from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import csv
from create_list import create_list
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

# Create a list of licenses
licences = create_list()
print(licences[:10], "  ", len(licences))
templist = []
for i in range(0, len(licences)):
    try:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(15)
        driver.get('https://omma.us.thentiacloud.net/webs/omma/register/#/business')
        search_input = driver.find_element(By.ID , 'keywords')
        search_input.send_keys(licences[i])
        submit_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/div/div/div/button')
        submit_button.click()
        time.sleep(1)
        licence_no = licences[i]
        business_name = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/table-builder/div[1]/table/tbody/tr/td[2]/strong').text
        licence_type = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/table-builder/div[1]/table/tbody/tr/td[3]').text
        city = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/table-builder/div[1]/table/tbody/tr/td[4]').text
        county = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/table-builder/div[1]/table/tbody/tr/td[5]').text
        expiration_date = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/table-builder/div[1]/table/tbody/tr/td[6]').text
        view_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/table-builder/div[1]/table/tbody/tr/td[7]/a')
        view_button.click()
        time.sleep(1)
        dba = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[2]/div').text
        if driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[5]/label/span').text == "Street Address:":
            street_address = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[5]/div').text
            zip_code = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[8]/div').text
            telephone_number = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[9]/div').text
            email = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[10]/div').text
            hours_of_operation = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[11]/div').text
        else:
            street_address = None
            zip_code = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[7]/div').text
            telephone_number = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[8]/div').text
            email = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[9]/div').text
            hours_of_operation = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/div/div[10]/div').text
        driver.close()
        print("Count: {}; Licence No: {}".format(i, licence_no))
        Table_dict = {
            'licence_type': licence_type,
            'license_no': licence_no,
            'business_name': business_name,
            'dba': dba,
            'street_address': street_address,
            'zip_code': zip_code,
            'city': city,
            'county': county,
            'telephone_number': telephone_number,
            'email': email,
            'hours_of_operation': hours_of_operation,
            'expiration_date': expiration_date
        }
        templist.append(Table_dict)
        df = pd.DataFrame(templist)
        df.to_csv('table.csv')
    except NoSuchElementException:
        print("Count {}; No such element found".format(i))
        df = pd.DataFrame(templist)
        df.to_csv('table.csv')
df = pd.DataFrame(templist)
df.to_csv('table.csv')


