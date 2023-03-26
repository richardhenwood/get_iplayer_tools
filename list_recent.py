
import csv
from datetime import datetime, timedelta, timezone
from collections import OrderedDict

available_idx = 8
last_n_days = 1
prog_dict = {}

with open('tv.cache', newline='\n') as csvfile:
    tvlist = csv.reader(csvfile, delimiter='|')
    first_row = True
    for row in tvlist:
        if first_row:
            first_row = False
            continue
        ava = row[available_idx]
        dt = datetime.fromisoformat(ava)
        if dt not in prog_dict:
            prog_dict[dt] = []
        prog_dict[dt].extend(row)

dict1 = OrderedDict(sorted(prog_dict.items()))

new_shows = []

for dt, show in dict1.items():
    older_dt = datetime.now(timezone.utc) - timedelta(days=last_n_days)
    if dt > older_dt: 
        new_shows.append(show)
    
for show in new_shows:
    print(show[2])