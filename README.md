# Brickset Scraper Using Scrapy

## Intro

A Web Scraper that uses Python3 and Scrapy to scrape [Brickset](https://brickset.com/) - A LEGO database.

## Requirements

* Python 3.x
* Scrapy

## Usage

    scrapy runspider brickset-scraper > brickset-scraper.json

Example output JSON files are [here](./example-output).

By default, past 5 years of bricksets are scraped.

Change the START_YEAR and END_YEAR in [scraper.py](./scraper.py) to scrape desired years.

## Caveat

Example output has been beautified with [JSON Lint](https://jsonlint.com/) for readability.


Working of this web scraper depends on the source at [Brickset](https://brickset.com/).

Working as on 18 Aug 2018.

Foundation for this scraper can be found [here](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3).
