import scrapy
from ..items import GanjizufangItem


class Crawl(scrapy.Spider):
    name = "ganjizufang"   # 爬虫名，可以有多个，不重复名
    start_urls = ["http://hf.ganji.com/fang5/h2/"]  # 链接列表，可以多个

    def parse(self, response):  # 爬取成功后自动回调函数
        # print(response)

        zf = GanjizufangItem()

        title_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        money_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        roomsnum_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[1]/text()").extract()
        square_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[3]/text()").extract()
        direct_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[5]/text()").extract()
        floor_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[7]/text()").extract()
        decoration_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[2]/span[9]/text()").extract()
        community_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[3]/span/a[1]/text()").extract()
        address_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[3]/span/text()").extract()

        for i, j, k, l, m, n, o, p, q in zip(title_list, money_list, roomsnum_list, square_list, direct_list, floor_list,
                                       decoration_list, community_list, address_list):
            zf['title'] = i
            zf['money'] = j
            zf['roomsnum'] = k
            zf['square'] = l
            zf['direct'] = m
            zf['floor'] = n
            zf['decoration'] = o
            zf['community'] = p
            zf['address'] = q
            yield zf
        #     print(i, ":", j)