#!/usr/bin/python
# coding:utf8

import calendar
from datetime import datetime

today=datetime.today()
print(calendar.month(today.year, today.month))
