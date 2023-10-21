import scrapy


class LinkedinDirectoryScraperSpider(scrapy.Spider):
    name = "linkedin_directory_scraper"

    start_urls = [
        "https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies"]

    letter_nav_links = ['https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/a?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/b?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/c?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/d?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/e?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/f?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/g?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/h?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/i?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/j?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/k?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/l?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/m?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/n?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/o?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/p?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/q?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/r?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/s?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/t?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/u?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/v?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/w?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/x?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/y?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/z?trk=companies_directory_letter_nav',
                        'https://webcache.googleusercontent.com/search?q=cache:https://www.linkedin.com/directory/companies/more?trk=companies_directory_letter_nav']

    company_listings = {}

    def parse(self, response):
        featured_company_listings = response.css(".listings__entry-link")

        for i in range(0, len(featured_company_listings) - 1):
            self.company_listings[featured_company_listings[i].css(
                "::text").get()] = featured_company_listings[i].css("::attr(href)").get()

        letter_nav_tracker = 0
        first_url = self.letter_nav_links[letter_nav_tracker]

        yield scrapy.Request(url=first_url, callback=self.parse_response, meta={'letter_nav_tracker': letter_nav_tracker})

    def parse_response(self, response):
        letter_nav_tracker = response.meta['letter_nav_tracker']

        print('****')
        print(
            f'Scraping SECTION: {self.letter_nav_links[letter_nav_tracker].split("/")[-1].strip("?")[0].upper()}')
        print('****')

        company_listings = response.css(".listings__entry-link")

        for i in range(0, len(company_listings) - 1):
            self.company_listings[company_listings[i].css(
                "::text").get()] = company_listings[i].css("::attr(href)").get()

        print("Parsing Page and getting Company Listings..")

        yield self.company_listings

        letter_nav_tracker += 1

        if letter_nav_tracker <= (len(self.letter_nav_links) - 1):
            letter_nav_tracker += 1
            next_section_url = self.letter_nav_links[letter_nav_tracker]
            yield scrapy.Request(url=next_section_url, callback=self.parse_response, meta={'letter_nav_tracker': letter_nav_tracker})
