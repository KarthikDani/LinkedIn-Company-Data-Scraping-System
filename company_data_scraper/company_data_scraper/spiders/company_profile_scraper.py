import json
from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response
import re

input_file = 'directorydata.json'
target_company_info = "OpenAI"

def get_url_by_company_name(company_name):
    try:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)
            for company_data in data:
                if company_name in company_data:
                    return company_data[company_name]
    except FileNotFoundError:
        print(f"Error: JSON file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred while reading JSON file: {str(e)}")
    return None


class CompanyProfileScraperSpider(scrapy.Spider):
    name = 'company_profile_scraper'

    company_pages = [
        str(get_url_by_company_name(target_company_info))
        # 'https://in.linkedin.com/company/adani-electricity?trk=companies_directory'
        # 'https://www.linkedin.com/company/amazon?trk=companies_directory',
        # 'https://www.linkedin.com/company/google?trk=companies_directory',
        # 'https://www.linkedin.com/company/linkedin?trk=companies_directory'
    ]

    def start_requests(self):
        company_index_tracker = 0

        # self.readUrlsFromJobsFile()

        first_url = self.company_pages[company_index_tracker]
        yield scrapy.Request(url=first_url, callback=self.parse_response,
                             meta={'company_index_tracker': company_index_tracker})

    def parse_response(self, response):
        company_index_tracker = response.meta['company_index_tracker']
        print('********')
        print(
            f'Scraping page: {str(company_index_tracker + 1)} of {str(len(self.company_pages))}')
        print('********')

        company_item = {}

        company_item['company_name'] = response.css('.top-card-layout__entity-info h1::text').get(
            default='not-found').strip()

        company_item['linkedin_followers_count'] = int(response.xpath(
            '//h3[contains(@class, "top-card-layout__first-subline")]/span/following-sibling::text()').get().split()[
            0].strip().replace(',', ''))
        # attr(src) didn't work, I saw the img element response and found out `src` has changed to `data-delayed-url` for which there was logo link.
        company_item['company_logo_url'] = response.css(
            'div.top-card-layout__entity-image-container img::attr(data-delayed-url)').get('not-found')

        company_item['about_us'] = response.css('.core-section-container__content p::text').get(
            default='not-found').strip()

        try:
            followers_num_match = re.findall(r'\d{1,3}(?:,\d{3})*',
                                             response.css('a.face-pile__cta::text').get(default='not-found').strip())
            if followers_num_match:
                company_item['num_of_employees'] = int(
                    followers_num_match[0].replace(',', ''))
            else:
                company_item['num_of_employees'] = response.css('a.face-pile__cta::text').get(
                    default='not-found').strip()
        except Exception as e:
            print("Error occurred while getting number of employees: {e}")

        try:
            company_details = response.css(
                '.core-section-container__content .mb-2')

            company_item['website'] = company_details[0].css(
                'a::text').get(default='not-found').strip()

            company_industry_line = company_details[1].css(
                '.text-md::text').getall()
            company_item['industry'] = company_industry_line[1].strip()

            company_size_line = company_details[2].css(
                '.text-md::text').getall()
            company_item['company_size_approx'] = company_size_line[1].strip().split()[
                0]

            company_headquarters = company_details[3].css(
                '.text-md::text').getall()
            if company_headquarters[0].lower().strip() == 'headquarters':
                company_item['headquarters'] = company_headquarters[1].strip()
            else:
                company_item['headquarters'] = 'not-found'

            company_type = company_details[4].css('.text-md::text').getall()
            company_item['type'] = company_type[1].strip()

            # specialities or founded, one among them -> storing in `unsure_parameter`
            unsure_parameter = company_details[5].css(
                '.text-md::text').getall()
            unsure_parameter_key = unsure_parameter[0].lower().strip()
            company_item[unsure_parameter_key] = unsure_parameter[1].strip()
            # `founded` comes before specialties if exists, or else `specialties` at first means that `founded` parameter isn't defined
            if unsure_parameter_key == 'founded':
                company_specialties = company_details[6].css(
                    '.text-md::text').getall()
                # after `founded` is extracted, check if `specialties` is defined
                if company_specialties[0].lower().strip() == 'specialties':
                    company_item['specialties'] = company_specialties[1].strip()
                else:
                    company_item['specialties'] = 'not-found'
            elif unsure_parameter_key != 'specialties' or unsure_parameter_key == 'founded':
                company_item['founded'] = 'not-found'
                company_item['specialties'] = 'not-found'

            # funding parameters, more feasible error handling to be implemented, if sir needs to have..
            company_item['funding'] = response.css(
                'p.text-display-lg::text').get(default='not-found').strip()
            company_item['funding_total_rounds'] = int(response.xpath(
                '//section[contains(@class, "aside-section-container")]/div/a[contains(@class, "link-styled")]//span[contains(@class, "before:middot")]/text()').get(
                'not-found').strip().split()[0])
            company_item['funding_option'] = response.xpath(
                '//section[contains(@class, "aside-section-container")]/div//div[contains(@class, "my-2")]/a[contains(@class, "link-styled")]/text()').get(
                'not-found').strip()
            company_item['last_funding_round'] = response.xpath(
                '//section[contains(@class, "aside-section-container")]/div//div[contains(@class, "my-2")]/a[contains(@class, "link-styled")]//time[contains(@class, "before:middot")]/text()').get(
                'not-found').strip()

        except IndexError:
            print("Error: *****Skipped index, as some details are missing*********")

        yield company_item

        company_index_tracker += 1

        if (company_index_tracker <= len(self.company_pages) - 1):
            next_url = self.company_pages[company_index_tracker]
            yield scrapy.Request(url=next_url, callback=self.parse_response,
                                 meta={'company_index_tracker': company_index_tracker})
