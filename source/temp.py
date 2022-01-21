# import sys
# import time
# import random
from datetime import date
# from requests.models import LocationParseError
# import simple_twit as st
import TonyAPI as tony
import regex as re
# tony.deleteAccount("philongbui3".lower(), "account_0")

# # str = "!a @tony Calories 102"
# command = re.match(r'\!(.) @[a-zA-Z0-9]* ([a-zA-Z]*) ([0-9]*)', str)

# # print(command.group(1))
# # print(command.group(2))
# # print(command.group(3))
# print(tony.deleteGraph("philongbui3", "account_0", "studytime"))
today = date.today()
print("Today's date:", str(today).replace("-", ""))
