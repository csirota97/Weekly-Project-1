import requests
import bs4
import csv

res = requests.get("https://weather.com/weather/tenday/l/USDC0001:1:US")
weather_csv = "weather.csv"
type(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')
type(soup)

date = soup.select(".date-time")
day = soup.select(".day-detail")
temp = soup.select(".temp")
hum = soup.select(".humidity")

# i = 1
# while i < len(hum):
    # print(date[i-1].getText(), " - ", day[i-1].getText(), " - ", temp[i].getText(), " - ", hum[i].getText())
    # i += 1

with open(weather_csv,'w') as csvfile:
    fieldnames = ['Date','Day','Temperature', 'Humidity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    i = 1
    while i < len(hum):
        writer.writerow({'Date': date[i-1].getText(),'Day': day[i-1].getText(), 'Temperature': temp[i].getText(),'Humidity': hum[i].getText()})
        i += 1
