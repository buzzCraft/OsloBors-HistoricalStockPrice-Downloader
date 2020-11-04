# -*- coding: utf-8 -*-
"""
Yahoo finance scrapper
"""


#Need unixtime to paste in the url's
import time
import datetime
d = datetime.date(2020,10,29)

unixtime = time.mktime(d.timetuple())
print(unixtime)