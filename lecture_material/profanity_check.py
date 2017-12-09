#!/usr/bin/python
# coding=utf-8
import urllib


def read_text():
    quotes = open("")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print (output)
    connection.close()


check_profanity("test")
