# right now there is not support for .club.
# this has been released on master, but hasn't been pushed to pypi yet.
# this is fucking stupid, but ok, lets just get it working for .net for now.
import whois
import datetime

sites_to_check = [
    'jowj.net',
]

current_year = datetime.datetime.today().year

for site in sites_to_check:
    expire_year = whois.query(site).expiration_date.year
    if expire_year - current_year <= 1:
        pass  # throw an alert, check into sending email / sending to slack
