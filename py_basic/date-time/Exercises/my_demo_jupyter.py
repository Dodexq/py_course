# %%
import time
# %%
time.time()
# %%
epoch = time.gmtime(0)
epoch
# %%
now = time.localtime()
now
# %%
day_in_seconds = 60*60*24
yestarday = time.localtime(time.time() - day_in_seconds)
yestarday
# %%
print(time.localtime().tm_year, "year")
print(yestarday.tm_mon, "month", yestarday.tm_mday, "day")
# %%
time.asctime(time.localtime())
time.strftime('%B, %Y',time.localtime())
# %%
import datetime
# %%
date_today = datetime.date.today()
date_today
# %%
week_in_seconds = 24*60*60*7
datetime.date.fromtimestamp(week_in_seconds)
# %%
i_day = datetime.date(2022, 9, 7)
i_day.year, i_day.month, i_day.day
# %%
i_day.timetuple()

# %%
i_day.replace(year=2021)
i_day.replace(minute=24)
i_day.ctime()

# %%
dtime_today = datetime.datetime(year=2022, month=9, day=7,
hour=13, minute=14, second=15)
dtime_today.year, dtime_today.month, dtime_today.day
# %%
dtime_today.time()
dtime_tuple = dtime_today.timetuple()
dtime_tuple
# %%
