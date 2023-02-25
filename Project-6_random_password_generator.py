#this program returns the random password of required length which includes alphanumeric characters and special characters too.

import string
import random

def generate(password_length):

    allchars=list(string.ascii_letters+string.digits+"!@#$%^&*()")

    random.shuffle(allchars)  # shuffling the list so randomness increases

    password=[] # an empty list

    for x in range(password_length):  # selecting random chars from allchars list and adding to password list
        password.append(random.choice(allchars))

    random.shuffle(password) # increase more randomness

    password="".join(password) # join method takes a list and converts the list of elements into a string and concatenate to the given string(here->"")

    print("password:"+password)


password_length=int(input("enter the required length of password"))
generate(password_length)