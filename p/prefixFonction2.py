#!/usr/bin/env python
#-*- coding: utf-8 -*-

# use regular expression and csv
from re import sub, match, IGNORECASE
from csv import reader

def myFonction(csvFile, prefix):
    #declare list to put words
    myList=[]

    # open the list file
    with open(csvFile, "r", encoding="utf_8") as words:
        for word in (reader(words)):
            word=sub('[\[\]\']', '', str(word))
            if match(prefix, word, IGNORECASE)!= None:
                print(word, end=", ")

myFonction("country_list.csv", 'a')
