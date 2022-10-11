# Yelp API Scraper
This is a tool used for querying the Yelp API based on a set of geographic locales.

## What You Need
To use this tool, you will need:
* __A CSV file__ that includes a list of geograhpic areas and their corresponding latitude and longitudes :globe_with_meridians:
    * _Example Formatting:_

        | CBSA Code | City/Metro Area | Latitude | Longitude |
        | ------- | ------- | ------- | ------- |
        | 41180 | St. Louis | 38.8197 | -90.4502 |

* __A Yelp API key.__ You can ask Taelor Candiloro for her key or generate your own using the [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3/authentication). Save your API key as a Python file called APIKeys.py in the same folder as this script. I've provided a sample APIKey.py template that you can add your key to if you'd like.
* __Know what category you're searching for.__ You will need to edit the script to tell it what category (or type) of business to search for. Accepted category inputs can be found on [Yelp's developer site](https://www.yelp.com/developers/documentation/v3/all_category_list).

## How to Use
1. __Make sure all your files are in the same folder.__ You should at least have the Yelp Scraper, your CSV file of geographic areas, and your API Keys in the same folder.
2. __Edit the CATEGORY variable in the script.__ Insert your desired Yelp category as a string variable. Change CATEGORY variable in the script.
    *_Example:_
        ```
        CATEGORY = "hotels"
        ```
3. __Edit the name of the CSV output.__ Change the OUTPUT_FILE variable to what you want the CSV output file to be named.
    *_Example:_
        ```
        OUTPUT_FILE = "hotels.csv"
        ```
