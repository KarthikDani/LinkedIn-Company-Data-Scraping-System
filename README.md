# LinkedIn Company Data Scraping System

The LinkedIn Company Data Scraping System combines two powerful spiders for extracting valuable data from LinkedIn: `Linkedin Directory Scraper` and `Company Profile Scraper` python files. 
This system provides a comprehensive solution for gathering company information for various purposes, including research, analytics, building solutions and more.

## Table of Contents

1. [Features](#1-features)
2. [Installation](#2-installation)
3. [Usage](#4-usage)
4. [Data Output](#5-data-output)
5. [Contributing](#7-contributing)

## 1. Features

- **Scalability**: Extract thousands of company profiles without being blocked by LinkedIn.
- **Customizable**: Define your own data collection parameters and filters.
- **Data Output**: Export data in a structured JSON format for easy integration into your workflows.
- **Comprehensive**: Gather company names, associated URLs, and detailed company profile information

- **User-Agent Rotation**: Automatically rotate user agents to avoid detection and blocking by LinkedIn.
- **Crawler Control**: Customize crawling speed and frequency to avoid overloading LinkedIn's servers.
- **Data Analysis**: Perform data analysis, visualization, and other research activities to gain insights into the LinkedIn company profiles you have scraped.

## 2. Installation

To set up the LinkedIn Company Data Scraping System, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/KarthikDani/LinkedIn-Company-Data-Scraping-System.git
# 2. Go into each of the folder
cd LinkedIn-Company-Data-Scraping-System

# 3. (Optional) To create a virtual environment [exists in this case already]
python3 -m venv venv

# 4. Activate the virutal environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# 5. Install required packages
pip install scrapy requests
```

## 3. Usage

### LinkedIn Company Directory Scraper

Run the LinkedIn Company Directory Scraper using the following command:

```bash
scrapy crawl linkedin_directory_scraper -O directory_data.json
```

The scraped company directory data will be stored in the `directory_data.json` file in a structured JSON format or use `directory_data.csv`, according to your convinience.

### LinkedIn Company Profile Scraper

To Populate the list of companies you want to get information about, it's important to understand that the `company_profile_scraper.py` is supposed to take list of company names, through which it grabs the respective linkedin urls from the `directorydata.json` that scrapes the specific urls.

Go to `company_profile_scraper.py` and add your list of companies in the given `desired_company_names` list. You can add as many as you like!

```python
desired_company_names = ["Microsoft", "OpenAI"] # Please make sure to check the spellings of the names given
```

Run the LinkedIn Company Profile Scraper using the following command:

```bash
scrapy crawl company_profile_scraper -O company_profile_data.json
```

The scraped company profile data will be stored in the `company_profile_data.json` file in a structured JSON format.

## 5. Data Output

### LinkedIn Company Directory Scraper Output

The extracted directory data will be structured as follows:

```json
[
  {
    "company_name_1": "url of the company",
    "company_name_2": "url of the company",
    ...
  }
]
```
The Project is capable of extracting ~ 2 Lakh company names along with their linkedin page URLs from the Linkedin Company Directory.

### LinkedIn Company Profile Scraper Output

The extracted company profile data will include details such as company name, LinkedIn followers count, company logo URL, about us section, number of employees, website, industry, company size, headquarters, type, founding year, specialties, funding details, and last funding round information.

Below is an example of the output format of the company profile scraper with 16 useful and distinct parameters.

```json
[
    {
        "company_name": "OpenAI",
        "linkedin_followers_count": 2610704,
        "company_logo_url": "https://media.licdn.com/dms/image/C4E0BAQG0lRhNgYJCXw/company-logo_200_200/0/1678382029586?e=2147483647&v=beta&t=ixFAwvTgLyU99x2ihJEGBuy0T-Mp6lenxo_fDUJP3vY",
        "about_us": "OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. AI is an extremely powerful tool that must be created with safety and human needs at its core. OpenAI is dedicated to putting that alignment of interests first — ahead of profit.\n\nTo achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity. Our investment in diversity, equity, and inclusion is ongoing, executed through a wide range of initiatives, and championed and supported by leadership.\n\nAt OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.",
        "num_of_employees": 1230,
        "website": "https://openai.com/",
        "industry": "Research Services",
        "company_size_approx": "201-500",
        "headquarters": "San Francisco, CA",
        "type": "Partnership",
        "founded": "2015",
        "specialties": "artificial intelligence and machine learning",
        "funding": "not-found",
        "funding_total_rounds": 10,
        "funding_option": "Secondary market",
        "last_funding_round": "Sep 14, 2023"
    }
]

```


## 6. Contributing

Contributions to this project are welcome! Whether you have bug fixes, feature enhancements, or ideas to share, please create issues or submit pull requests to help improve this LinkedIn Company Data Scraping System.
