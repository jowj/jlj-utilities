# utils
this repo houses some random shit i wrote that does stuff for me. almost no one will want this stuff.

## dwim-youtube-dl
youtube-dl is fucking amazing. its one of the coolest / most useful things maintained by oss people that regular, normal humans see. but it doesn't do what i want it to do out of the box.

### features
- assumes everything is part of a playlist
- each file downloaded goes in a folder named after the playlist

- declare a flag that determines what library the target should go to
  - video vs audio right now
  
## get-domain-status
using the whois package, get the status of my domains. send an email under the following conditions:
- the domain is < 90 days away from expiring
- the SSL is < 30 days away from expiring

### todo:
- [ ] wait until the .club tld support is merged in, add my other domains to the list of shit to check
- [ ] add SSL checking to the script
- [ ] add email / slack alerting to the script.
- [ ] eventually move this to the `arke` project so that its deployed to my servers and alerted on consistently

# DWIM naming history

dwim comes from someone in the history of LISP. i like the connotation of doing what /i/, in particular, mean, rather than the general 'try and figure out what i mean' that it has in history.

besides, based on the critics of the DWIM system i feel like my interpretation is more accurate anyway.
https://en.wikipedia.org/wiki/DWIM#Software
