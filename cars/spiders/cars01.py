import scrapy
import pandas as pd



chrome_path = r"C:\Users\haqab\Desktop\DS\chromedriver.exe"

class Cars01Spider(scrapy.Spider):
    name = 'cars01'
    #allowed_domains = ['https://www.olx.in/']
    start_urls = ['https://www.olx.in/en/item/toyota-etios-vd-2012-diesel-iid-1595588005']
    
    # def parse(self,response):
    #     df = pd.read_csv(r'C:\Users\haqab\Desktop\DS\cars\output_cars.csv')
    #     prices_price = df['URL'].tolist()
    #     for i in prices_price:
    #         #print(prices_price)
    #         yield scrapy.Request(str(i), callback = self.parselevel1)
        
    def parse(self, response):

        name = response.xpath('//*[@class = "_3rJ6e"]/text()').extract_first()
        manufacture = response.xpath('//*[@class = "_18gRm"]/text()').extract_first()
        location = response.xpath('//*[@class = "_2FRXm"]/text()').extract_first()
        price = response.xpath('//*[@class = "_2xKfz"]/text()').extract_first()
        

        yield {
            
            'URL' : response.url, 
            'Company_name' : name,
            'Price' : price,
            'Location' : location,
            'Manufacture' : manufacture
        }
