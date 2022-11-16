import scrapy
from ..items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://talentedge.com/iit-delhi/operations-management-and-analytics-course",
        "https://talentedge.com/xlri-jamshedpur/financial-management-course",
        "https://talentedge.com/xlri-jamshedpur/human-resource-management-course",
        "https://talentedge.com/iim-kozhikode/professional-certificate-program-marketing-sales-management-iim-kozhikode",
        "https://talentedge.com/iim-kozhikode/professional-certificate-programme-in-hr-management-and-analytics"
    ]

    def parse(self, response):
        items = QuoteItem()
        title = response.xpath("//title/text()").extract()
        short_des = response.xpath('//p[@class="mb-0"]/text()').extract()
        des = response.xpath('//div[@class="desc"]/p/text()').extract()

        def skills():
            key_skills = response.xpath('//div[@class="key-skills-sec"]/ul/li/text()').extract()
            res = ('|').join(key_skills)

            return res

        def Eligibility():
            eligibility = response.xpath('//div[@class="eligible-right-top-list"]/ul/li/text()').extract()
            res = '|'.join(eligibility)
            return res
        def Syllabus():
            Module = response.xpath('//div[@class="sylab-tab-ul"]/ul/li/a/text()').extract()

            modules = ""


            headcount = 1

            for mod in Module:
                mod = mod.strip()
                # if mod == "\n":
                #     break
                header = f"<p>MODULE{headcount}: {mod}"
                modules += str(header)


                temp = response.xpath(f'//*[@id="syl-tab{headcount}"]/ul/li/text()').extract()
                if temp is not None:
                    for submod in temp:
                        sub = f"<br/>{submod}"
                        modules += sub
                modules += "</p>"
                modules += "\n"
                headcount += 1

            modules = ''.join(str(modules).split(','))
            return modules

        amount = response.xpath("//div[@class='program-details-total-pay-amt-right']/text()").extract_first()

        Amount = amount.replace(" ", "")
        Amount = Amount.replace("\n", " ")
        Amount = Amount.replace("+ GST", "")
        yield {
            'title': title,
            'short description': short_des,
            'description': des,
            'key skills': skills(),
            'Pre-requisites': Eligibility(),
            'Syllabus': Syllabus(),
            'Amount': Amount
        }

















