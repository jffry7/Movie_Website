#!/usr/bin/python
# coding=utf-8

import time
import webbrowser

number_breaks = 3
for i in range(0, number_breaks):
    time.sleep(5)
    webbrowser.open("https://www.google.com/")
