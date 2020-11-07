import scrapy
from selenium import webdriver
import time


chrome_path = r"C:\Users\haqab\Desktop\DS\chromedriver.exe"

class ccSpider(scrapy.Spider):
    name = 'cc'
    #allowed_domains = ['https://www.olx.in/']
    start_urls = ['https://www.olx.in/cars_c84']
    
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_path)
    
    def parse(self, response):
        self.driver.get(response.url)
        
        # time.sleep(1)
        # #for loading more pages, Clicking on load pages 
        # for i in range(1,3):
        #     time.sleep(1)
        #     next = self.driver.find_element_by_xpath('//*[@class="rui-3sH3b rui-3K5JC rui-1zK8h"]')
        #     next.click()
        
        time.sleep(2)
        # Extracting cars links
        haq = self.driver.find_elements_by_xpath('//*[@class = "EIR5N"]/a')
        links = [] # array of cars links
        
        for j in haq:
            links.append(j.get_attribute('href'))
        #print(links) # output...
        

        # extracting individual links for continueing with next page, detailed approach.. 
        for x in links:
            yield scrapy.Request(str(x), callback = self.parse_level2)

    # Scraping page
    def parse_level2(self, response):
        
        # data to scrape... 
        
        com_name = response.xpath('//*[@data-aut-id = "value_make"]/text()').extract_first()
        
        yield {
            'company_name' : com_name,
        }
