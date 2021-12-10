#!/usr/bin/env python
#-*- coding: utf-8 -*-

##############################
###Concevez un script qui reçoivent comme paramètres un fichier CSV et un préfixe et qui retourne tous les mots du fichier commençant par ce préfixe.###
##############################

# use regular expression and csv
import re
import csv

# declare the prefix
prefix="a"

# open the verb file
with open("verb_list.csv", encoding="utf_8") as v_list:
    for verb in (csv.reader(v_list)):
        # replace the list to string and clean the text
        verb=re.sub('[\[\]\']', '', (str(verb)))
        # print if starts with prefix
        if verb.startswith(prefix):
            print(verb)
