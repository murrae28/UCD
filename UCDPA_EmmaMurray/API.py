import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=G3AIAWSMKK6WO6H9'
r = requests.get(url)
data = r.json()
print(r.text)


