from matplotlib.cbook import index_of
import requests
import datetime

class Service():
    @staticmethod
    def get_data(dateFrom, dateTo, holiday):
        results = []
        dates = []
        weatherInfo = []
        temps = []
        avTemp = 0
        avTemps = []
        linkHolidays = "https://date.nager.at/api/v3/publicholidays/%s/PL"
        linkWeather = "https://www.metaweather.com/api/location/523920/%d/%d/%d"

        for x in range(dateFrom, dateTo+1):
            request = requests.get(linkHolidays % x).json()
            results.append(request)
                
        for x in results:
            for y in x:
                if y['localName'] == holiday:
                    dates.append(y['date'])
        
        for x in dates:
            d = datetime.datetime.strptime(x, "%Y-%m-%d")
            request = requests.get(linkWeather % (d.year,d.month,d.day)).json()
            weatherInfo.append(request)

        for x in weatherInfo:
            for y in x:
                temps.append(y['the_temp'])
            for i in temps:
                avTemp += i
            avTemp //= len(temps)
            avTemps.append(avTemp)
            temps.clear()
            avTemp = 0
        
        for x in range(len(dates)):
            print(str(dates[x]) + " = " + str(avTemps[x]))
    

Service.get_data(2017, 2021, "Wielkanoc")
