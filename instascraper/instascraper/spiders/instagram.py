import scrapy
from urllib3.parse import urlencode
import json
from datetime import datetime
API = 'YOURAPIKEY'
user_accounts = ["dedszead"] 

def start_requests(self):
    for username in user_accounts:
        url = f'https://www.instagram.com/{username}/?hl=en'
        yield scrapy.Request(get_url(url), callback=self.parse)

class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['http://instagram.com/']

    def parse(self, response):
        pass
