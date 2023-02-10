import requests

COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "UYF9LNZV8K96S6PC"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NAME = "TSLA"

NEWS_API_KEY = "92bed4237ee147c7b87228ad35246f8d"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# Get stock data
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / day_before_yesterday_closing_price) * 100, 0)

if abs(diff_percent) > 0.5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title",
        "sortBy": "relevancy",
        "language": "en",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"][:3]
    formatted_articles = [f'{STOCK_NAME}: {up_down}{diff_percent}\nHeadline: {article["title"]}.\nBrief: {article["description"]}' for article in news_data]

    for article in formatted_articles:
        print(article)
