# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest, Request

from .config import login_credentials # like {'user':'username','pwd':'password','town': '','redirect': '','mid': ''}

class PermitSpider(Spider):
    name = 'PermitScraper'
    allowed_domains = ['sdlportal.com']
    # start_urls = ['https://www.sdlportal.com/towns/nj/hudson/jerseycity/search?st=permits&amp;q=+&amp;limit=1000&amp;stps=all&amp;kw=&amp;stpd=yesterday&amp;psd=0&amp;ped=0&amp;ug=all']
    start_urls = ['https://www.sdlportal.com/towns/nj/hudson/jerseycity/search?st=permits&amp;q=+&amp;limit=1000&amp;stps=all&amp;kw=&amp;stpd=last7&amp;psd=0&amp;ped=0&amp;ug=all']

    def parse(self, response):
        return FormRequest.from_response(response,formdata=login_credentials,callback=self.scrape_index)


    def scrape_permit_details(self, response): # see https://stackoverflow.com/questions/37257870/scrapy-getting-data-from-links-within-table

        permit = response.meta["permit"] # import the permit summary

        td_fields = ['Description', 'Comments', 'Use Group', 'Related Permits', 'Total Construction Costs', 'Permit Fee', 'DCA State Fee','Total Due','Total Paid','Remaining Balance']


        table_content = response.xpath('//*[@class="table-responsive"]//tr')

        # search the page's tables for each field row
        for field in td_fields:

            # and extract the data
            for row in table_content:  # todo debug permit detail field matching loop
                current_td_scrape_field_name = row.xpath('td[1]//text()').extract_first()
                current_td_scrape_field_content = row.xpath('td[2]//text()').extract_first()

                # todo if field = 'Related Permits'
                if field == current_td_scrape_field_name:
                    permit[field] = current_td_scrape_field_content
                    pass

        yield permit


    def scrape_index(self, response): # per https://www.simplified.guide/scrapy/scrape-table

        for row in response.xpath('//*[@class="table table-striped table-bordered table-paginate  table-download "]//tr'):

            # CRAWL PERMIT SUMMARY
            permit_summary = {
                'control_number' : row.xpath('td[1]//text()').extract_first(),
                'url' : row.xpath("td[1]/a/@href").extract_first(),
                'permit_number' : row.xpath('td[2]//text()').extract_first(),
                'issue_date' : row.xpath('td[3]//text()').extract_first(),
                'location' : row.xpath('td[4]//text()').extract_first(),
                'owner': row.xpath('td[5]//text()').extract_first(),
                'work_type' : row.xpath('td[6]//text()').extract_first(),
                'work_description' : row.xpath('td[7]//text()').extract_first(),
                'subcodes' : row.xpath('td[8]//text()').extract_first(),
                'status' : row.xpath('td[9]//text()').extract_first()
            }           

            # CRAWL PERMIT DETAIL
            # try:
            #     yield Request(permit_summary['url'], meta={"permit": permit_summary}, callback=self.scrape_permit_details)
            # except:
            #     yield
            yield Request(permit_summary['url'], meta={"permit": permit_summary}, callback=self.scrape_permit_details)

