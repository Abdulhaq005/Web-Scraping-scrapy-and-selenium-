import scrapy


chrome_path = r"C:\Users\haqab\Desktop\DS\chromedriver.exe"

class Cars01Spider(scrapy.Spider):
    name = 'cars01'
    #allowed_domains = ['https://www.olx.in/']
    start_urls = ['https://www.olx.in/cars_c84']
    
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_path)
    
    def parse(self,response):
        cities_ = response.xpath('//*[@class="_396bV _2zs4P _1nXYG"]').extract()
        for city in cities_:     
            i = city.xpath('//@href').extract_first()
            yield scrapy.Request(str(city), callback = self.parselevel1)
            
    def parselevel1(self, response):
        for j in range(1, 15):
            try:
            time.sleep(1)
            # for clicking load more botton
            load_more = self.driver.find_element_by_xpath('//*[@class="rui-3sH3b rui-3K5JC rui-1zK8h"]')
            load_more.click()
            
            # escaping errors
        except NoSuchElementException:
            pass
        
    # car links
    # main links of cars to scrape.
    posts = self.driver.find_elements_by_xpath('//*[@class = "EIR5N"]/a')
    links = [elem.get_attribute('href') for elem in posts]
    
    # checking the output
    #print(len(links)) # len of the output links.. 
    for i_ in links:
        yield scrapy.Request(str(i_), callback = self.parselevel2)     
            
    def parselevel2(self, response):
        
        try:
            url = self.driver.find_element_by_xpath('//*[@rel = "alternate"]')
            URL = url.get_attribute('href')
            #URL.append(url.get_attribute('href'))
            name = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_make"]').text
            price = self.driver.find_element_by_xpath('//*[@class="_18gRm"]').text
            local = self.driver.find_element_by_xpath('//*[@class="_2FRXm"]').text
            model = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_model"]').text 
            variant = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_variant"]').text
            year = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_year"]').text 
            fuel = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_petrol"]').text
            transmission = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_transmission"]').text
            mileage = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_mileage"]').text 
            no_owner = self.driver.find_element_by_xpath('//*[@data-aut-id = "value_first_owner"]').text


        except NoSuchElementException:
            pass
        
        
        yield {
            
            'URL' : URL, 
            'Company_name' : name,
            'Price' : price,
            'Location' : local,
            'Model' : model, 
            'Variant' : variant, 
            'Year' : year, 
            'Fuel' : fuel, 
            'Transmission' : transmission, 
            'Mileage' : mileage, 
            'No_owner' : no_owner, 
            
        }
