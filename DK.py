import requests
from bs4 import BeautifulSoup

def scrape_prizepicks_by_category(category):
    # Base URL of the website
    base_url = "https://sportsbook.draftkings.com/"

    # Constructing the URL based on the category
    url = f"{base_url}leagues/basketball/ncaab"

    # Sending an HTTP GET request to the URL
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting information based on the structure of the website
        props = soup.find_all('div', class_='sportsbook-league-page__body')

        # Printing out the results
        print(f"Props in the {category} category:")
        for prop in props:
            prop_title = prop.find('div', class_='sportsbook-table_body').text.strip()
            prop_description = prop.find('div', class_='sportsbook-table__column-row').text.strip()
            print(f"Title: {prop_title}")
            print(f"Description: {prop_description}")
            print("----------------------------------------")
    else:
        print("Failed to retrieve data")

# Example usage:
category = "Soccer"  # Specify the category you want to scrape
scrape_prizepicks_by_category(category)
