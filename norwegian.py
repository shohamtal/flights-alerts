import requests
from datetime import datetime
from BeautifulSoup import BeautifulSoup
from flight_scraper import FlightScrapper


class NorwegianScrapper(FlightScrapper):
    def __init__(self):
        pass

    def _day(self, dt):
        return datetime.strftime(dt, "%d")

    def _monthyear(self, dt):
        return datetime.strftime(dt, "%Y%m")


    def get_rates(self, fly_out_date, fly_back_date, fly_from, fly_to):
        # dates sample 2017/03/26
        # fly_from sample 'TLV'

        d_out = self._day(fly_out_date)
        moye_out = self._monthyear(fly_out_date)
        d_back = self._day(fly_back_date)
        moye_back = self._monthyear(fly_back_date)
        currency = 'EUR'

        url = 'https://www.norwegian.com/en/booking/flight-tickets/select-flight/?A_City={fly_to}&AdultCount=1' \
              '&ChildCount=0&CurrencyCode={currency}&D_City={fly_from}&D_Day={d_out}&D_Month={moye_out}&IncludeTransit=true' \
              '&InfantCount=0&R_Day={d_back}&R_Month={moye_back}&TripType=2'.format(
            currency=currency, d_out=d_out, moye_out=moye_out, d_back=d_back, moye_back=moye_back,
            fly_from=fly_from, fly_to=fly_to)
        res = requests.get(url)
        if res.status_code >= 400:
            res.raise_for_status()

        soup = BeautifulSoup(res.content)
        tables = soup.findAll("table", {"class": "avadaytable"})

        fly_to_rates = []
        trs = tables[0].find('tbody').findAll('tr')
        for tr in trs:
            if 'rowinfo1' in tr['class']:
                tds = tr.findAll('td')
                for td in tds:
                    if 'fareselect' in td['class']:
                        lbl = td.find('div').find('label')
                        fly_to_rates.append(int(float(lbl.text)))

        fly_back_rates = []
        trs = tables[1].find('tbody').findAll('tr')
        for tr in trs:
            if 'rowinfo1' in tr['class']:
                tds = tr.findAll('td')
                for td in tds:
                    if 'fareselect' in td['class']:
                        lbl = td.find('div').find('label')
                        fly_back_rates.append(int(float(lbl.text)))

        return fly_to_rates, fly_back_rates, url


class KiwiScrapper(FlightScrapper):
    def __init__(self):
        raise NotImplementedError
        pass

    def _day(self, dt):
        return datetime.strftime(dt, "%d")

    def _monthyear(self, dt):
        return datetime.strftime(dt, "%Y%m")


    def get_rates(self, fly_out_date, fly_back_date, fly_from, fly_to):
        # dates sample 2017/03/26
        # fly_from sample 'TLV'

        d_out = self._day(fly_out_date)
        moye_out = self._monthyear(fly_out_date)
        d_back = self._day(fly_back_date)
        moye_back = self._monthyear(fly_back_date)
        currency = 'EUR'

        url = 'https://www.kiwi.com/il/search/me%E1%BA%96oz-tel-aviv-medinat-yisra%E2%80%99el-250km/london-united-kingdom/2017-04-16/2017-04-20?daysInWeek=0-4'

        url2 = 'https://www.norwegian.com/en/booking/flight-tickets/select-flight/?A_City={fly_to}&AdultCount=1' \
              '&ChildCount=0&CurrencyCode={currency}&D_City={fly_from}&D_Day={d_out}&D_Month={moye_out}&IncludeTransit=true' \
              '&InfantCount=0&R_Day={d_back}&R_Month={moye_back}&TripType=2'.format(
            currency=currency, d_out=d_out, moye_out=moye_out, d_back=d_back, moye_back=moye_back,
            fly_from=fly_from, fly_to=fly_to)
        res = requests.get(url)
        if res.status_code >= 400:
            res.raise_for_status()

        soup = BeautifulSoup(res.content)
        tables = soup.findAll("div", {"class": "Sorting-content"})

        fly_to_rates = []
        trs = tables[0].find('tbody').findAll('tr')
        for tr in trs:
            if 'rowinfo1' in tr['class']:
                tds = tr.findAll('td')
                for td in tds:
                    if 'fareselect' in td['class']:
                        lbl = td.find('div').find('label')
                        fly_to_rates.append(int(float(lbl.text)))

        fly_back_rates = []
        trs = tables[1].find('tbody').findAll('tr')
        for tr in trs:
            if 'rowinfo1' in tr['class']:
                tds = tr.findAll('td')
                for td in tds:
                    if 'fareselect' in td['class']:
                        lbl = td.find('div').find('label')
                        fly_back_rates.append(int(float(lbl.text)))

        return fly_to_rates, fly_back_rates, url
