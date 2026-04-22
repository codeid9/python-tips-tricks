from datetime import datetime
from datetime import date

time_now = datetime.now().strftime('%H:%M:%S')
print(f'The time now is {time_now}')

today_date = date.today()
print(today_date)