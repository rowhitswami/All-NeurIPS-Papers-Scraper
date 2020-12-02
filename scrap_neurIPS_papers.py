#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Quick script to scrap and save all NeurIPS papers
    
    Author: Rohit Swami
    Email: rowhitswami1@gmail.com
    GitHub: https://www.github.com/rowhitswami
"""

# Importing necessary libraries
import requests
import argparse
import pandas as pd
from tqdm import tqdm
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup, SoupStrainer

# Initializing argeparse
parser = argparse.ArgumentParser(description='Script to scrap NeurIPS Papers')
parser.add_argument('-start', action="store", default=1987, dest="start_year", type=int, help='The start year to scrap the papers')
parser.add_argument('-end', action="store", default=2019, dest="end_year", type=int, help='The end year to scrap the papers')
arguments = parser.parse_args()

# Argeparse conditions
if arguments.start_year < 1987 or arguments.start_year > 2019:
    raise ValueError("Please enter a valid start year. Possible values are [1987, 2019].")

if arguments.end_year < 1987 or arguments.end_year > 2019:
    raise ValueError("Please enter a valid end year. Possible values are [1987, 2019].")

if arguments.start_year > arguments.end_year:
    raise ValueError("Start year shouldn't be greater than end year. Possible values are [1987, 2019].")

# Constants
BASE_URL = "https://papers.nips.cc/paper/"
PARSER = 'lxml'
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
}
start_year = arguments.start_year
end_year = arguments.end_year
papers = []
paper_authors = []


def get_conference_url(start_year, end_year):
    """Return all the URLs of conferences between start_year and end_year"""

    conferences = []
    print("Preparing data...")
    for year in tqdm(range(start_year, end_year+1)):
        year_url = BASE_URL + str(year)
        conferences.append({"URL": year_url})
    return conferences


def get_all_hashes(url):
    """
        Context: The NeurIPS website follow a structured pattern by maintaining a hash for each paper.

        Return all the hashes for a particular year.
    """
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, PARSER)

            hashes = []
            for li in soup.find("div", class_="container-fluid").find_all("li"):
                paper_url = li.a.get('href')
                paper_hash = paper_url.split("/")[-1].split("-")[0]
                hashes.append(paper_hash)
            return hashes
        else:
            print("Couldn't complete the request.")
            return False
    except ConnectionError as error:
        print(error)


def scrap_paper_and_authors(year_url, hashes):
    """Scrap papers and authors using extracted hashes"""

    for paper_hash in tqdm(hashes):
        paper_url = year_url + "/file/" + paper_hash + "-Metadata.json"
        try:
            response = requests.get(paper_url, headers=HEADERS)
            if response.status_code == 200:
                doc = response.json()

                # Extracting paper
                paper = {}
                paper['source_id'] = doc['sourceid']
                paper['year'] = year_url.split("/")[-1]
                paper['title'] = doc['title']
                paper['abstract'] = doc['abstract'] if doc['abstract'] else None
                paper['full_text'] = doc['full_text']
                papers.append(paper)

                # Extracting authors from a paper
                for author in doc['authors']:
                    author_details = {}
                    author_details['source_id'] = doc['sourceid']
                    author_details['first_name'] = author['given_name'] if author['given_name'] else None
                    author_details['last_name'] = author['family_name'] if author['family_name'] else None
                    author_details['institution'] = author['institution'] if author['institution'] else None
                    paper_authors.append(author_details)
            else:
                print("Couldn't complete the request.")
                break
        except ConnectionError as error:
            print(error)


def save_file(file_name, data):
    """Converting a list of dicts to Pandas dataframe and saving it as a CSV File"""

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False, header=True)
    print(f"Successfully saved {file_name}")

# Getting all conferences
conferences = get_conference_url(start_year, end_year)

# Scrapping papers and authors
for year in conferences:
    hashes = get_all_hashes(year["URL"])
    if hashes:
        scrap_paper_and_authors(year["URL"], hashes)

# Saving data as a CSV file
if papers and paper_authors:
    save_file("papers.csv", papers)
    save_file("paper_authors.csv", paper_authors)
else:
    print("Couldn't save the files!")
