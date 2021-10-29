# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item


class ScrapperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UdemyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    id = Field()
    instructors = Field()
    description = Field()
    price = Field()
    link = Field()
    source = Field()


class UdacityItem(Item):
    title = Field()
    id = Field()
    instructors = Field()
    level = Field()
    prerequisites = Field()
    description = Field()
    price = Field()
    source = Field()
