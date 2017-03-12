
crontab -e

# add this..
# it will execute the script every 15 mins and write the output into log file:

*/15 * * * * python /var/www/flights-alerts/run.py > /var/www/flights-alerts/cronlog.log 2>&1

