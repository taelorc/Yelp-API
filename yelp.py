import json
import requests
import csv
import time
import pandas as pd
from sqlalchemy import null
from APIKeys import * # includes credentials

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
INPUT_FILE = "city.csv"
RADIUS = 40000

# These are the two variables you should change
# change OUTPUT_FILE to what you want the CSV output file to be named
OUTPUT_FILE = "beer_wine_spirits.csv"

# change CATEGORY to the business category you want - here's the category list https://www.yelp.com/developers/documentation/v3/all_category_list
CATEGORY = "beer_and_wine"



count = []
average_rating = []
average_expense = []

cities = pd.read_csv(INPUT_FILE)

for index,row in cities.iterrows():

    LATITUDE = row['latitude']
    LONGITUDE = row['longitude']

    LIMIT = 50

    response = requests.get(
        API_HOST+SEARCH_PATH,
        params={'categories': CATEGORY, 'latitude': LATITUDE, 'longitude': LONGITUDE, 'limit': LIMIT, 'radius': RADIUS},
        headers={'Authorization': 'Bearer %s' % API_KEY},
    )
    y = response.json()
    print(row)
    print(y["total"])
    i = 0
    total_rating = 0
    expense = " "
    total_expense = 0
    while (i < len(y["businesses"])):
        total_rating += y["businesses"][i]["rating"]
        if "price" in y["businesses"][i]:
            expense = y["businesses"][i]["price"]
            total_expense += len(expense)
        i = i + 1
    print(total_rating)
    print(total_expense)
    if i != 0:
        avg_rating = total_rating / i
        avg_expense = total_expense / i
        print(avg_rating)
        print(avg_expense)
    
    count.append(y["total"])
    average_rating.append(avg_rating)
    average_expense.append(avg_expense)
    time.sleep(5)

cities['count'] = count
cities['avg rating'] = average_rating
cities['avg expense'] = average_expense
cities.to_csv(OUTPUT_FILE)