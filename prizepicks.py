import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

def scrape_prizepicks_by_category(category):
    # Base URL of the website
    base_url = "https://app.prizepicks.com/"

    # Sending an HTTP GET request to the URL
    response = requests.get(base_url)

    #Creating table for players
    ppPlayers = []

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting information based on the structure of the website
        props = soup.find_all('div', class_={'name': 'SOCCER'})


        # Printing out the results
        print(f"Props in the {category} category:")
        for prop in props:
            prop_title = prop.find('div', class_='projection').text.strip()

            for projections in prop_title:
                names = projections.find(class_="name").text
                pts = projections.find(class_="score").get_attribute('innerHTML')
                proptype = projections.find(class_="text").get_attribute('innerHTML')
                print(f"Title: {prop_title}")
                print(f"Description: {projections}")
                print("----------------------------------------")

                players= {
                    'Name': names,
                    'Points': pts,
                    'Prop': proptype.replace("<wbr>", "")
                }
        ppPlayers.append(players)

        dfProps = pd.DataFrame(ppPlayers)
        filename = "pp.csv"

        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(dfProps)

        print("These are all of the props offered by PP.", '\n')
        print(dfProps)
        print('\n')


