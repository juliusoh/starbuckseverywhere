import requests
import pandas as pd

url = "http://www.starbuckseverywhere.net/StoreClosingDates.htm"

page = requests.get(url)

df = pd.read_html(url)[0]
# df.columns = ["Closed", "Name", "City", "Market"]
headers = df.iloc[0]
df = df[1:]
df.columns = headers
df.to_csv('data.csv', index= False)
print(df)

# starbucks_table = soup.findChildren('table')[0]

# rows = starbucks_table.findChildren(['th', 'tr'])

# for row in rows:
#     cells = row.find_all('td')
#     for cell in cells:
#         cellText = cell.text

