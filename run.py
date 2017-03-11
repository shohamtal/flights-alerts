import datetime

from norwegian import NorwegianScrapper
from slacker import Slacker


SLACK_BOT_TOKEN = 'xoxb-153794345367-sBk2dQZUCE3wu8VeS94rFyRf'
SLACK_CHANNEL = '#general'


def next_weekday(startdate, weekday):
    """
    @startdate: given date
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    t = datetime.timedelta((7 + weekday - startdate.weekday()) % 7)
    return (startdate + t)



days_delta = 4
today = datetime.date.today()
two_days_from_now = today + datetime.timedelta(days=2)
sunday1 = next_weekday(two_days_from_now, 6)
thursday1 = next_weekday(sunday1, 3)
sunday2 = next_weekday(sunday1+ datetime.timedelta(days=1), 6)
thursday2 = next_weekday(sunday2, 3)
sunday3 = next_weekday(sunday2+ datetime.timedelta(days=1), 6)
thursday3 = next_weekday(sunday3, 3)
sunday4 = next_weekday(sunday3+ datetime.timedelta(days=1), 6)
thursday4 = next_weekday(sunday4, 3)

dates_list = [(sunday1, thursday1), (sunday2, thursday2), (sunday3, thursday3), (sunday4, thursday4)]


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



