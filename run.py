from datetime import timedelta

from norwegian import *
from slacker import Slacker


SLACK_BOT_TOKEN = 'xoxb-153794345367-sBk2dQZUCE3wu8VeS94rFyRf'
SLACK_CHANNEL = '#general'


def next_weekday(startdate, weekday):
    """
    @startdate: given date
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    t = timedelta((7 + weekday - startdate.weekday()) % 7)
    return (startdate + t)



days_delta = 4
today = datetime.today().date()
two_days_from_now = today + timedelta(days=2)
sunday1 = next_weekday(two_days_from_now, 6)
thursday1 = next_weekday(sunday1, 3)
dates_list = [(sunday1, thursday1)]
for x in range(0, 14):
    prev_sun = dates_list[x][0]
    sun = next_weekday(prev_sun + timedelta(days=1), 6)
    thu = next_weekday(sun, 3)
    dates_list.append((sun, thu))


if __name__ == '__main__':
    fly_from = 'TLV'
    fly_to = 'LON'

    for sun, thu in dates_list:
        print 'Dates: ' + str(sun) + ' - ' + str(thu) + ' at Norwegian airlines: ---------------------------------------------------'
        norwegian = NorwegianScrapper()
        fly_to_rates, fly_back_rates, url = norwegian.get_rates(sun, thu, fly_from, fly_to)
        min_ticket = min(fly_to_rates) + min(fly_back_rates)
        if min_ticket <= 170:
            msg = 'min ticket found at price of: ' + str(min_ticket) + 'url: ' + url
            print msg
            slack = Slacker(SLACK_BOT_TOKEN)
            slack.chat.post_message(SLACK_CHANNEL, msg)
        else:
            print 'NOT cheap: ' + str(min_ticket)



