# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: Phi Long Bui
# netid:  lpbui
# Student ID: 114555975

import sys
import time
import random

from requests.models import LocationParseError
import simple_twit as st
import TonyAPI as tony
import regex as reg
from datetime import date

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "MAfC3oKYmRIYt0m0I1Lcw5voX"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "NyQKSHLTCuI7TW25XKN7qtk5dcmT3l4qNxldjfqrNuoVk5DYTp"

# Project 04 Exercises

# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text


def exercise1(api):
    t = st.get_home_timeline(api, 10)
    for i in range(0, 10):
        json = t[i]._json
        print(f"---------Tweet {i+1}------------")
        print(f"ID: {json['id']}")
        print(f"Author: {json['user']['name']}")
        print(f"author's screen_name: {json['user']['screen_name']}")
        print(f"Created Date: {json['created_at']}")
        print(f"tweet full text: {json['full_text']}")

 # remove this and replace with your solution code


# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    user = 'elonmusk'
    t = st.get_user_timeline(api, user, 10)

    for i in range(0, 10):
        json = t[i]._json
        print(f"---------Tweet {i+1}------------")
        print(f"ID: {json['id']}")
        print(f"Author: {json['user']['name']}")
        print(f"author's screen_name: {json['user']['screen_name']}")
        print(f"Created Date: {json['created_at']}")
        print(f"tweet full text: {json['full_text']}")


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    st.send_tweet(api, text="Hello World!")


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    st.follow_user(api, "IAE101114622347")

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
# TonyAPI need to be imported into this class.
num_acc = 0


def getListOfUser():
    # generate a user as a list contain data needed for the command to function.
    amount = 1
    listOfusers = []
    a = st.get_mentions(api, amount)
    for i in range(0, amount):
        user = []
        isCreated = False
        json = a[i]._json
        user.append(json['user']['screen_name'])
        user.append(json['id'])
        user.append(isCreated)
        str = json['full_text']
        # print("Tweet: " + str)
        msg = reg.match(r'\%(.) @.+', str).group(1)  # get the letter command
        # special case: g
        if msg == "g":
            temp = reg.match(r'\%(.) @[a-zA-Z0-9]* ([a-zA-Z]*) ([a-z]*)', str)
            user.append(temp.group(1))
            user.append(temp.group(2))
            user.append(temp.group(3))
            listOfusers.append(user)
            # special case: p
        elif msg == "p":
            temp = reg.match(r'\%(.) @[a-zA-Z0-9]* ([a-zA-Z]*) ([0-9]*)', str)
            user.append(temp.group(1))
            user.append(temp.group(2))
            user.append(temp.group(3))
            listOfusers.append(user)
            # normal case a, d
        elif msg == "a" or msg == "d":
            user.append(msg)
            listOfusers.append(user)
    return listOfusers


def getCurrentDate():
    # return current date as yyyymmdd
    today = date.today()
    return str(today).replace("-", "")

# This twitter bot is going to collect th tweet then analyze it to get command.
# a case, generate a tracking account
# d case, delete the tracking account
# g case, create a graph as your habit
# p case, update your graph with the amount of unit per day, make sure to delete the old p tweet before post another identical tweet.


def twitterbot(api):
    users = getListOfUser()
    for user in users:
        if user[3] == "a":
            if user[2] != True:
                temp = f'Hey @{user[0]}! {tony.createAccount(user[0].lower(), "account_" + str(num_acc))}'
                user[2] = True
                st.send_reply_tweet(api, temp, user[1])
        if (user[3]) == "d":
            temp = f'Hey @{user[0]}! {tony.deleteAccount(user[0].lower(), "account_" + str(num_acc))}'
            user[2] = False
            st.send_reply_tweet(api, temp, user[1])
        if (user[3]) == "g":
            name = user[4]
            unit = user[5]
            temp = f'Hey @{user[0]}! {tony.createGraph(user[0].lower(), "account_" + str(num_acc),name.lower(),name,unit)}'
            st.send_reply_tweet(api, temp, user[1])
        if (user[3]) == "p":
            id = user[4].lower()
            quantity = user[5]
            temp = f'Hey @{user[0]}! {tony.postPixel(getCurrentDate(),user[0].lower(),"account_" + str(num_acc),id,quantity)}'
            st.send_reply_tweet(api, temp, user[1])


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    st.version()
    api = st.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    # exercise1(api)
    # exercise2(api)
    # exercise3(api)
    # exercise4(api)
    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
