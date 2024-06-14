"""
project: project_3
author: Vo Minh Quan
email: minhquanvo18@gmail.com
discord: peterrrming
"""

import requests
from bs4 import BeautifulSoup
import csv
import argparse

BASE_URL = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'

def get_base_url(url):
    return url.rsplit('/', 1)[0]

def fetch_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}")
    return response.content

def parse_main_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')
    parsed_data = []

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            link = cells[0].find("a")
            if link:
                url_suffix = link.get("href")
                full_url = f"{get_base_url(BASE_URL)}/{url_suffix}"
                location_data = [cell.get_text(strip=True) for cell in cells[:2]]
                parse_secondary_page(full_url, parsed_data, location_data)
    
    return parsed_data

def parse_secondary_page(url, data_store, location_data):
    html_content = fetch_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')
    headers = []

    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 9:
            location_info = [cells[i].get_text(strip=True) for i in [3, 4, 8]]
            location_data.extend(location_info)
        elif len(cells) == 5:
            party_name = cells[1].get_text(strip=True)
            vote_count = cells[2].get_text(strip=True)
            location_data.append(vote_count)
            headers.append(party_name)
    
    if not data_store:
        headers = ['code', 'location', 'registered', 'envelopes', 'valid'] + headers
        data_store.append(headers)
    data_store.append(location_data)

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='cp1250') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

def main(url, output_file):
    html_content = fetch_html(url)
    parsed_data = parse_main_page(html_content)
    write_to_csv(parsed_data, output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web scraping script')
    parser.add_argument('url', type=str, help='URL of the website to scrape')
    parser.add_argument('output_file', type=str, help='Name of the output file')
    args = parser.parse_args()
    
    if not args.url or not args.output_file:
        print("Error: Both URL and output file name must be provided.")
    else:
        main(args.url, args.output_file)
