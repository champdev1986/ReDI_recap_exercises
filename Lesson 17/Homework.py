import requests
from requests.exceptions import HTTPError

GET_RANDOM_QUOTES = 'https://api.quotable.io/quotes/random'
AMOUNT_ARG = 'limit'
QUOTE_ID = '_id'
QUOTE_CONTENT = 'content'
QUOTE_AUTHOR = 'author'

def get_random_quotes(amount):
   try: 
      payload = {AMOUNT_ARG: amount}
      response = requests.get(GET_RANDOM_QUOTES, params = payload) 
      if response.status_code == 200:
         quotes_data = response.json()
         count = 0
         for quote in quotes_data:
            count += 1
            print(f"{count}. Quote\n{quote[QUOTE_CONTENT]}\nby {quote[QUOTE_AUTHOR]}\n\n")
            # print(f"{quote['id']}")
      else:
        print(f"Error: response status code = {response.status_code}") 
   except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')
   except Exception as err:
      print(f'Other error occurred: {err}')

get_random_quotes(5)