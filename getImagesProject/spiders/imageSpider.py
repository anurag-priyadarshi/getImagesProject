import scrapy
import csv
from getImagesProject.items import GetimagesprojectItem
from scrapy.spider import Spider
from scrapy.http.request import Request
class ImageSpider(Spider):
    allowed_domains = ['kay.com','macys.com','costco-static.com','fredmeyerjewelers.com','jared.com','imageg.net','jcpenny.com','bluenile.com']
    name = 'imageSpider'
    start_urls =[]
    
    def start_requests(self):
        with open('imageURLs.csv') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                item = GetimagesprojectItem()
                image_url = row['URL']
                item['image_urls'] = [row['URL'],]
                item['pid'] = row['ID']
                request = Request(image_url,callback = self.parse)
                request.meta['item'] = item
                yield request
    
    def parse(self, response):
        
        yield  response.meta['item']