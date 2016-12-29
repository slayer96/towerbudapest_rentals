# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TowerbudapestRentalsItem(Item):
    # define the fields for your item here like:
    url = Field()
    reference_number = Field()
    street_name = Field()
    district = Field()
    rooms = Field()
    size = Field()
    image_urls = Field()
    description = Field()
    floor = Field()
    parking = Field()
    view = Field()
    furnished = Field()
    elevator = Field()
    air_conditioner = Field()
    rental_fee = Field()
    phone_number = Field()
    # coordinate = Field() # !!!!

