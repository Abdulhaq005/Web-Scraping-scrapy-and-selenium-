#importing libraries 
import pandas as pd
from selenium import webdriver # for webdriver 
from selenium.common.exceptions import NoSuchElementException # for exception handling
import time # for delay


# setting platform for selenium
path = r'C:\Users\haqab\Desktop\DS\chromedriver.exe'
driver = webdriver.Chrome(path)

# url 
driver.get('https://www.olx.in/cars_c84')


# setting arrays for data. 
links = []
URL = []
Company_name = []
prices = []
Location = []
Model = []
Variant = []
Year = []
Fuel = []
Transmission = []
Mileage = []
No_owner = []

#main state wise url links
for i in pages:
    driver.get(i)
    for j in range(1,15):
        try:
            time.sleep(1)
            # for clicking load more botton
            load_more = driver.find_element_by_xpath('//*[@class="rui-3sH3b rui-3K5JC rui-1zK8h"]')
            load_more.click()
            
            # escaping errors
        except NoSuchElementException:
            pass
    
    
    # car links
    # main links of cars to scrape.
    posts = driver.find_elements_by_xpath('//*[@class = "EIR5N"]/a')
    links = [elem.get_attribute('href') for elem in posts]
    # checking the output
    #print(len(links))
    
    
    # individual cars url main scraping process..
    for i in links:
        driver.get(i)
        try:

            url = driver.find_element_by_xpath('//*[@rel = "alternate"]')
            #print(url.get_attribute('href'))
            URL.append(url.get_attribute('href'))

            name = driver.find_element_by_xpath('//*[@data-aut-id = "value_make"]').text
            #print(name)
            Company_name.append(name)

            price = driver.find_element_by_xpath('//*[@class="_18gRm"]').text
            #print(price)
            prices.append(price)

            local = driver.find_element_by_xpath('//*[@class="_2FRXm"]').text
            #print(local)
            Location.append(local.split(',')[2])

            model = driver.find_element_by_xpath('//*[@data-aut-id = "value_model"]').text 
            #print(model)
            Model.append(model)

            variant = driver.find_element_by_xpath('//*[@data-aut-id = "value_variant"]').text
            #print(variant)
            Variant.append(variant)

            year = driver.find_element_by_xpath('//*[@data-aut-id = "value_year"]').text 
            #print(year)
            Year.append(year)

            fuel = driver.find_element_by_xpath('//*[@data-aut-id = "value_petrol"]').text
            #print(fuel)
            Fuel.append(fuel)

            transmission = driver.find_element_by_xpath('//*[@data-aut-id = "value_transmission"]').text
            #print(transmission)
            Transmission.append(transmission)

            mileage = driver.find_element_by_xpath('//*[@data-aut-id = "value_mileage"]').text 
            #print(mileage)
            Mileage.append(mileage)

            no_owner = driver.find_element_by_xpath('//*[@data-aut-id = "value_first_owner"]').text
            #print(no_owner)
            No_owner.append(no_owner)


        except NoSuchElementException:
            pass

    #print('One state complete')
    
#print(len(links))
# The complete output

# conveting into dict..
dictt = {
    'URL' : URL,
    'Company_name' : Company_name,
    'prices' : prices,
    'Loctaion' : Location,
    'Model' : Model,
    'Varient' : Variant,
    'Year' : Year,
    'Fuel' : Fuel,
    'Transmission' : Transmission,
    'Mileage' : Mileage,
    'No_owner' : No_owner }
dictt

# saving to data frame using pandas
df2 = pd.DataFrame.from_dict(dictt, orient = 'index')
df2 = df.transpose()

# output file
df.to_csv('output.csv')
