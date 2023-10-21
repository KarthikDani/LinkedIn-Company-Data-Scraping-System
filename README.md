# LinkedIn Company Data Scraping System

The LinkedIn Company Data Scraping System combines two powerful tools for extracting valuable data from LinkedIn: the LinkedIn `Company Directory Scraper` and the LinkedIn `Company Profile Scraper`. 
This system provides a comprehensive solution for gathering company information for various purposes, including research, analytics, building solutions and more.

## Table of Contents

1. [Features](#1-features)
2. [Installation](#2-installation)
3. [Getting Started](#3-getting-started)
4. [Usage](#4-usage)
5. [Data Output](#5-data-output)
6. [Contributing](#7-contributing)

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
git clone https://github.com//linkedin-company-data-scraping-system.git
cd linkedin-company-data-scraping-system

## Go into each of the two folders and carry out the below mentioned steps
# 2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# 3. Install required packages
pip install scrapy requests
```

## 3. Getting Started

To start scraping LinkedIn company profiles and directory data, customize the project according to your requirements:

- Configure user agents and data sources in the respective settings files.

## 4. Usage

### LinkedIn Company Directory Scraper

Run the LinkedIn Company Directory Scraper using the following command:

```bash
scrapy crawl directoryspider -O directorydata.json
```

The scraped company directory data will be stored in the `directorydata.json` file in a structured JSON format or use `directorydata.csv`, according to your convinience.

### LinkedIn Company Profile Scraper

Run the LinkedIn Company Profile Scraper using the following command:

```bash
scrapy crawl company_profile -O companyprofiledata.json
```

The scraped company profile data will be stored in the `companyprofiledata.json` file in a structured JSON format.

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
We are currently capable of extracting approximately 2 Lakh company names along with their linkedin page URLs.

### LinkedIn Company Profile Scraper Output

The extracted company profile data will include details such as company name, LinkedIn followers count, company logo URL, about us section, number of employees, website, industry, company size, headquarters, type, founding year, specialties, funding details, and last funding round information.

Below is an example of the output format of the company profile scraper with 16 useful and distinct parameters.

```json
]    
    {
        "company_name": "Google",
        "linkedin_followers_count": 31591786,
        "company_logo_url": "https://media.licdn.com/dms/image/C4D0BAQHiNSL4Or29cg/company-logo_200_200/0/1519856215226?e=2147483647&v=beta&t=kJv1gX0_sqLG1g7LKLD5uh_6uEFpWGUTuzpuvVJVdEw",
        "about_us": "A problem isn't truly solved until it's solved for all. Googlers build products that help create opportunities for everyone, whether down the street or across the globe. Bring your insight, imagination and a healthy disregard for the impossible. Bring everything that makes you unique. Together, we can build for everyone.\n\nCheck out our career opportunities at goo.gle/3DLEokh",
        "num_of_employees": 288809,
        "website": "https://goo.gle/3DLEokh",
        "industry": "Software Development",
        "company_size_approx": "10,001+",
        "headquarters": "Mountain View, CA",
        "type": "Public Company",
        "specialties": "search, ads, mobile, android, online video, apps, machine learning, virtual reality, cloud, hardware, artificial intelligence, youtube, and software",
        "funding": "$130.44",
        "funding_total_rounds": 3,
        "funding_option": "Series A",
        "last_funding_round": "Jul 7, 1999"
    }
]

```


## 6. Contributing

Contributions to this project are welcome! Whether you have bug fixes, feature enhancements, or ideas to share, please create issues or submit pull requests to help improve this LinkedIn Company Data Scraping System.
