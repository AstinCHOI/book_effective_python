
## 1) time module (don't use to change other time zone)
from time import localtime, strftime

now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)
# >>>
# 2014-08-11 03:18:30


from time import mktime, strptime
time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)
# >>>
# 1407694710.0


# parse_format = '%Y-%m-%d %H:%M:%S %Z'
# depart_sfo = '2014-05-01 15:45:16 PDT'
# time_tuple = strptime(depart_sfo, parse_format)
# time_str = strftime(time_format, time_tuple)
# print(time_str)
# >>>
# ValueError: time data '2014-05-01 15:45:16 PDT' does not match format '%Y-%m-%d %H:%M:%S %Z'


# arrival_nyc = '2014-05-01 23:33:24 EDT'
# time_tuple = strptime(arrival_nyc, time_format)
# ValueError: unconverted data remains:  EDT


## 2) datetime module
# UTC -> Local time
import sys
if sys.version_info[0] >= 3:
    from datetime import datetime, timezone 
    now = datetime(2014, 8, 10, 18, 18, 30)
    now_utc = now.replace(tzinfo=timezone.utc)
    now_local = now_utc.astimezone()
    print(now_local)
# >>>
# 2014-08-11 03:18:30+09:00


time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)
# >>>
# 1407637110.0


## 3) pytz(https://pypi.python.org/pypi/pytz)
# NYC -> UTC
import pytz
arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print(utc_dt)
# >>>
# 2014-05-02 03:33:24+00:00

# UTC -> Sanfrancisco
pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)
# >>>
# 2014-05-01 20:33:24-07:00

# UTC -> Nepal
nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)
# >>>
# 2014-05-02 09:18:24+05:45