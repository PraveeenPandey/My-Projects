import scrapy
import ast
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QuestSpider(scrapy.Spider):

    name = "quests"
    allowed_domains = ["www.dataquest.io"]



    start_urls = ["https://www.dataquest.io/data-science-courses/individual-courses/"]



    # rules = (
    #     Rule(LinkExtractor(allow='course'), callback='parse_categories'),
    # )




    def parse(self, response):
        # global urls
        urls =  response.xpath('//script[@id="course-data"]//text()').extract_first()
        urls_dict = ast.literal_eval(urls)
        urls_key = urls_dict.keys()
        for key in urls_key:
            link = f'https://www.dataquest.io/course/{key}/'
            yield scrapy.Request(link, callback=self.parse_categories)

        # le = LinkExtractor(
        #     allow_domains=self.allowed_domains,
        #
        # )
        # for link in le.extract_links(response):
        #     yield scrapy.Request(
        #         url=link.url,
        #         callback=self.parse_categories,
        #
        #     )


    def parse_categories(self,response):
        # getting the complete text script from the website
        mod = response.xpath('//div[@class="content-wrap d-flex flex-column"]/script/text()').extract_first()
        # removes the new line from the list mod
        Mod = mod.strip()
        # converting list to dictionary
        data = ast.literal_eval(Mod)

        # getting the desired data using key with the dictionary
        title = data['name']
        short_des = data['description']
        des = response.xpath('//div[@class="row"]/p/text()').extract_first()

        # get the Key Skills
        key_skills = data['objectives']
        res = (',').join(key_skills)

        # gets the Course Outline
        lessons = data['lessons']
        length = len(lessons)
        #formatting the content part
        content = '<?xml version = "1.0"?>' +'<main module>'
        module_count = 1

        #for loop to iterate through the list lesson which contains all the modules and sub-modules
        ##of course outline
        for lesson_num in range(length):
            content += f'<module{module_count}>'
            content += f'<heading>{lessons[lesson_num]["name"]}</heading>'
            content +=  '<subheading>'
            course = lessons[lesson_num]
            course_length = len(course['objectives'])
            # for loop to iterate through the dict(course) key:-list(objectives)
            item_count = 1
            for course_count in range(course_length):
                content += f'<item{item_count}>{course["objectives"][course_count]}</item{item_count}>'
                item_count += 1
            content +=  '</subheading>'
            content += f'</module{module_count}>'


            module_count += 1
        content += '</main module>'

        # for e.g. output of rate: '4.8 (359 reviews)'
        rate = response.xpath('//div[@class="media pb-3"]/p/text()').extract_first()
        # rating = '4.8'
        rating = rate[0:3]

        sign_ups = data['signups']
        lesson_count = data["lesson_count"]
        learn_type = response.xpath('//div[@class="text-inner pt-3"]/ul/li/text()')[1].extract()
        level = response.xpath('//div[@class="text-inner pt-3"]/ul/li/text()')[0].extract().replace('friendly','')


        #INSTRUCTOR KPI's
        Instructor_img = response.xpath('//div[@class="image-holder border-dark border-1 d-flex align-items-center"]/img/@src').extract_first()
        Instructor_name = response.xpath('//h4[@class="m-0"]/text()').extract_first()
        Instructor_des = response.xpath('//p[@class="small mb-2"]/text()').extract_first()
        Instructor_desig = response.xpath('//span[@class="small"]/text()').extract_first()

        site_url = response.url



        Amount = response.xpath('//*[@id="course-enroll-button"]/text()').extract_first()



        yield {
            'site url': site_url,
            'title': title,
            'short description': short_des,
            'description': des,
            'Skills': res,
            'content_main_description': content,
            'Rating': rating,
            'Sign_ups': sign_ups,
            'Lesson Count': lesson_count,
            'Learn Type':learn_type,
            'Level':level,
            'Instructor Name': Instructor_name,
            'Instrutor Designation': Instructor_desig,
            'Instructor Description': Instructor_des,
            'Instructor Image': Instructor_img,
            'Amount': Amount,

        }