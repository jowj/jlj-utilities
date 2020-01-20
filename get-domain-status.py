# right now there is not support for .club.
# this has been released on master, but hasn't been pushed to pypi yet.
# this is fucking stupid, but ok, lets just get it working for .net for now.
import whois
from datetime import datetime
import OpenSSL
import ssl
import pdb

domains_to_check = [
    'jowj.net',
]

sites_to_check = [
    'me.jowj.net',
    'bouncer.awful.club',
    'my.awful.club',
    'matrix.awful.club'
]

current_year = datetime.today().year
today = datetime.today()

for domain in domains_to_check:
    expire_year = whois.query(domain).expiration_date.year

    # if the domain expires in ~1yr or less, throw alert
    if expire_year - current_year <= 1:
        pass  # throw an alert, check into sending email / sending to slack

for site in sites_to_check:
    cert = ssl.get_server_certificate((site, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    # pdb.set_trace()
    expiration = datetime.strptime(x509.get_notAfter().decode(), '%Y%m%d%H%M%SZ')

    if (expiration - today):
        pass  # throw an alert, check into sending email / sending to slack
