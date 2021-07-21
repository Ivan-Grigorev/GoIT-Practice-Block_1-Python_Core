# from datetime import datetime
#
#
# d1 = datetime.now()
# my_dict = {'milk': datetime(year=2021, month=6, day=30),
# 'butter': datetime(year=2021, month=8, day=2),
# 'jogurt': datetime(year=2021, month=7, day=12)}
# answer = []
# for key, val in my_dict.items():
#     if val >= d1:
#         answer.append(key)
# print(answer)
#

#
# from datetime import datetime, timedelta
#
#
# d1 = datetime.now()
# count = 0
# while datetime.now() - d1 <= timedelta(seconds=5):
#     count += 1
# print(count)


from datetime import time, datetime, timedelta, tzinfo


import pytz
d1 = datetime.now()
d2 = time(8, 15, 12, 0, pytz.UTC+2)
print(d2)
print(d1.strftime("%A/%B/%Y"))




