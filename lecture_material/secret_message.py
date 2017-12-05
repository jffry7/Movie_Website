#!/usr/bin/python
# coding=utf-8
import os


def rename_files():
    file_list = os.listdir(r"C:\prank")
    saved_path = os.getcwd()
    print "Current path is " + saved_path
    os.chdir(r"C:\prank")
    for filename in file_list:
        print "Old name " + filename
        print "New name " + filename.translate(None, "0123456789")
        os.rename(filename, filename.translate(None, "0123456789"))
    os.chdir(saved_path)


rename_files()
