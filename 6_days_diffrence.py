from datetime import date
from_date = date(2019, 7, 2)
last_date = date(2018, 7, 11)
delta = from_date - last_date
print(delta.days)