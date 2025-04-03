from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import csv
from core.logging import logger
from fastapi.responses import FileResponse

app = FastAPI()


# Creating a get request
def get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors (4xx,5xx)
        logger.info(f"URL {url} opened correctly")
        return response
    except requests.exceptions.InvalidURL:
        logger.error(f"Invalid Url: The given {url} is incorrect")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")

    return None  # Return None if requests fails


# Function to parse data
def parsing_response_data(response):
    if response is None:
        logger.error(f"No response received, skipping parsing")
        return []

    try:
        bs = BeautifulSoup(response.text, "html.parser")
        # Find all quote page elements
        quote_elements = bs.find_all("div", class_="quote")
        logger.info(f"Response was parsed,{len(quote_elements)} html elements were retrieved")
        return quote_elements
    except Exception as e:  # General exception for BeautifulSoup errors
        logger.error(f"Error parsing response : {str(e)}")
        return []


# Create lists to store quotes and authors
def extracting_quotes_authors(quote_elements):
    if not quote_elements:
        logger.warning(f"No quote elements found, skipping data extraction")
        return []

    try:
        # Extracting of data using list comprehension instead of for loop
        authors_quotes = [
            (quote_div.find("span", class_="text").text.strip(),
             quote_div.find("small", class_="author").text.strip())
            for quote_div in quote_elements
        ]
        logger.info(f"Quotes and authors combined successfully and found = {len(authors_quotes)} records")
        return authors_quotes

    except Exception as e:
        logger.error(f"Error in extracting quotes and authors:{str(e)}")


# Writing and saving data to file
def writing_to_file(authors_quotes, filename):
    if not authors_quotes:
        logger.warning(f"No data to write, skipping file writing")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8-sig") as file:  # Use of utf-8-sig adds Byte Order Mark
            writer = csv.writer(file)
            # header
            writer.writerow(["Quotes", "Author"])
            writer.writerows(authors_quotes)
        logger.info(f"File {filename} is updated successfully")
    except IOError as e:
        logger.error(f"Could not write to the file {filename}:{str(e)}")


# FastAPI endpoint for scrapping quotes
@app.get("/scrape-quotes")
async def scrapping_quotes(url: str):
    logger.info(f"Starting web scrapping for URL: {url}")
    #url = "https://quotes.toscrape.com/"

    # Scrape the data
    response = get_request(url)
    quote_elements = parsing_response_data(response)
    authors_quotes = extracting_quotes_authors(quote_elements)
    writing_to_file(authors_quotes, "quotes_of_authors.csv")

    # Return CVS file as a download
    return FileResponse("quotes_of_authors.csv", media_type="text/csv", filename="quotes_of_authors.csv")


'''
quotes = []
        authors = []

        # Looping through quote elements
        for quote_div in quote_elements:

            # Extract quote text
            #print(quote_div.find("span",class_="text").text)
            quote = quote_div.find("span", class_="text").text
            quotes.append(quote)

            # Extract author text
            author = quote_div.find("small", class_="author").text
            #print(author)
            authors.append(author)

            #print(quotes)
            #print(authors)

            # Combine quotes and authors
        authors_quotes = list(zip(quotes, authors))
        #print(authors_quotes)
'''