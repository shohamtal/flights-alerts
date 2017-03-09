from datetime import datetime
from norwegian import NorwegianScrapper


if __name__ == '__main__':
    from_date = '2017/03/26'
    to_date = '2017/03/30'
    fly_from = 'TLV'
    fly_to = 'LGW'

    print 'Norwegian airlines check ---------------------------------------------------'
    norwegian = NorwegianScrapper()
    fly_to_rates, fly_back_rates, url = norwegian.get_rates(from_date, to_date, fly_from, fly_to)
    min_ticket = min(fly_to_rates) + min(fly_back_rates)
    if min_ticket <= 170:
        print 'min ticket found at price of: ' + str(min_ticket)
        print 'url : ' + url
    else:
        print 'NOT cheap: ' + str(min_ticket)



