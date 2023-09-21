# LinkedIn Company Directory Scraper

![GitHub last commit](https://img.shields.io/github/last-commit/[KarthikDani/LinkedIn-Company-Directory-Scraper](https://github.com/KarthikDani/LinkedIn-Company-Directory-Scraper/))
![GitHub license](https://img.shields.io/github/license/KarthikDani/Linkedin-Company-Directory-Scraper)
![GitHub stars](https://img.shields.io/github/stars/KarthikDani/Linkedin-Company-Directory-Scraper?style=social)

## Table of Contents

1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Installation](#3-installation)
4. [Getting Started](#4-getting-started)
5. [Usage](#5-usage)
6. [Data Output](#6-data-output)
7. [Project Structure](#7-project-structure)
8. [LinkedIn Company Profile Scraper](#8-linkedin-company-profile-scraper)
9. [Contributing](#9-contributing)

## 1. Introduction

LinkedIn Company Directory Scraper is a publicly available tool for extracting company names and their associated URLs from LinkedIn's company directory. This project allows you to gather valuable data for various purposes, including marketing, research, and analytics.

## 2. Features

- **Scalability**: Capable of extracting thousands of company profiles without being blocked by LinkedIn.
- **Customizable**: Define your own data collection parameters and filters.
- **Data Output**: Export data in a structured JSON format for easy integration into your workflows.

## 3. Installation

To set up the LinkedIn Company Directory Scraper, follow these steps:

```bash

# 1. Clone the repository
git clone https://github.com/KarthikDani/linkedin-company-directory-scraper.git
cd linkedin-company-directory-scraper

# 2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

## 4. Getting Started

To start scraping LinkedIn company profiles, you can customize the project according to your requirements:

- Customize the user agent in the `settings.py` file.

## 5. Usage

Run the scraper using the following command:

```bash
scrapy crawl directoryspider -O directorydata.json
```

The scraped company data will be stored in the `directorydata.json` file in a JSON format.

## 6. Data Output

The extracted data will be structured as follows:

```json
[
  {
    "company_name_1": "url of the company",
    "company_name_2": "url of the company",
    ...
  }
]
```

## 7. Project Structure

- `linkedin_company_directory_scraper/`: The main project directory.
  - `spiders/`: Contains the Scrapy spider for scraping LinkedIn company profiles.
  - `settings.py`: Configuration file for defining scraping parameters.

## 8. LinkedIn Company Profile Scraper

For more comprehensive LinkedIn scraping, check out our [LinkedIn Company Profile Scraper](https://github.com/KarthikDani/linkedin-company-profile-scraper) repository. This project allows you to extract detailed information from individual LinkedIn company profiles.

## 9. Contributing

Contributions to this project are welcome! Whether you have bug fixes, feature enhancements, or ideas to share, please create issues or submit pull requests to help improve this LinkedIn Company Directory Scraper.
