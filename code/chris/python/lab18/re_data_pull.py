'''
Python mini-Capstone: Web Crawling for Property Tax Information

- https://techrando.com/2020/08/09/how-to-web-scrape-a-asp-net-web-form-using-selenium-in-python/

selenium for automated browser interaction and crawling
sendgrid for gmail interaction (version 2)


STAND-UPS: 
1) what did you do yesterday
2) what are you going to do today
3) what are your blockers (if any)

'''

from selenium import webdriver # had to pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd # https://pandas.pydata.org
import time

def data_pull(input_address):
    '''Takes an address and searches for it on Honolulu Tax Website.'''
    RE_driver = webdriver.Safari() # this establishes the session
    RE_driver.get('https://qpublic.schneidercorp.com/Application.aspx?App=HonoluluCountyHI&PageType=Search') # opens the safari window
    RE_driver.maximize_window()
    RE_driver.implicitly_wait(2)

    terms_and_conditions_agree = RE_driver.find_element(By.LINK_TEXT, 'Agree') # method found on geeksforgeeks
    terms_and_conditions_agree.send_keys(Keys.ENTER)

    address_field = RE_driver.find_element(By.ID, "addressSearchDiv31342")
    address_field.click()

    address_field.send_keys(input_address + Keys.ENTER)

    time.sleep(2)

    try:
        RE_driver.find_element(By.ID, "ctlBodyPane_ctl00_ctl01_gvwParcelResults_ctl03_lnkParcelID").send_keys(Keys.ENTER)
    except:
        print('One property found.')

    time.sleep(2)

    df = pd.DataFrame(columns = ["Assessment Year", "Property Class", "Assessed Land Value", # Create a dataframe to store all of the store all of the scraped data
    "Dedicated Use Value", "Land Exemption", "Net Taxable Land Value", 
    "Assessed Building Value", "Building Exemption", "Net Taxable Building Value",
    "Total Property Assessed Value", "Total Property Exemption", "Total Net Taxable Value"])

    for n in range(2, 15): # Flip through all of the records and save them
        for i in range(3): # secondary FOR loop w try-except, attempt pull data 3 times, prevents bottle necks
            try:
                mytable = RE_driver.find_element(By.ID, 'ctlBodyPane_ctl03_ctl01_gvValuationHistorical')
                table_body = mytable.find_element(By.TAG_NAME, 'tbody')
                for row in table_body.find_elements(By.TAG_NAME, 'tr'):
                    row_list=[]
                    # Add to dataframe accordingly
                    for cell in row.find_elements(By.TAG_NAME, 'td'):
                        cell_reading = cell.text
                        row_list.append(cell_reading)
                    # Add the list to a row, if possible
                    try:
                        a_series = pd.Series(row_list, index = df.columns)
                        df = df.append(a_series, ignore_index=True)
                    except:
                        print("Could not append: " + str(row_list))
                break
            except:
                RE_driver.implicitly_wait(10)

    df.drop_duplicates(inplace = True) # remove duplicates
    df.to_csv("property_tax_info.csv", index=False) # write to a CSV

    RE_driver.quit()

def value_cleanup(prop_value):
    '''Removes dollar signs and commas ($,) from value and converts to type int().'''
    value_trans = prop_value.maketrans('','','$,') # defines the table to translate the string (remove $,)
    tax_value = float(prop_value.translate(value_trans))
    return tax_value

def tax_calc(tax_int):
    '''Performs property tax calc: (value/1000) * 3.5 = $amt'''
    prop_taxes = (tax_int / 1000) * 3.5
    prop_taxes = round(prop_taxes, 2)
    return prop_taxes
    