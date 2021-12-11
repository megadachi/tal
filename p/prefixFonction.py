#!/usr/bin/env python
#-*- coding: utf-8 -*-

# use regular expression and csv
from re import sub, match, IGNORECASE
from csv import reader

def myFonction(csvFile, prefix):
    # open the list file
    with open(csvFile, "r", encoding="utf_8") as words:
        for word in (reader(words)):
            #clean the text
            word=sub('[\[\]\']', '', str(word))
            #if the word starts with prefix, print it
            if match(prefix, word, IGNORECASE)!= None:
                print(word)


myFonction("country_list.csv", 'a')
