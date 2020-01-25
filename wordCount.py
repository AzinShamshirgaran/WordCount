#!/usr/bin/env python
import collections, operator, re, string, sys
import pyodbc as db
from nltk.tokenize import wordpunct_tokenize
from collections import Counter
import numpy as np
import nltk
from nltk.corpus import stopwords
import sqlite3



def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

def stop_word_removal(fname):
  stop_words = set(stopwords.words('english'))
  for key in stop_words:
         del fname[key]
  return fname

if __name__ == "__main__":
  
  con = db.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=.;Trusted_Connection=yes;DATABASE=company')
  #con = sqlite3.connect("company.db")
  word_dic = word_count("MasterAllUnionAddress.txt")
  #word_dic = word_count("testt.txt")
  #print(len(word_dic))
  word_dic_wo_stop=stop_word_removal(word_dic)
  #print(word_dic_wo_stop)
  cur = con.cursor()
  #termId INTEGER PRIMARY KEY,
  sql_command = """
  CREATE TABLE TermIndex ( 
  term VARCHAR(8000), 
  count INTEGER);"""
  termidd=1
#  cur.execute(sql_command)
 # con.commit()

  for key,value in word_dic_wo_stop.items():
    format_str = """INSERT INTO TermIndex (term, count) VALUES ('{termm}', '{countt}');"""
    termidd =+ 1
    #print(value)
    sql_commandd = format_str.format(termm=key, countt=value)
    cur.execute(sql_commandd)
    con.commit()
  cur.execute("SELECT * FROM TermIndex") 
  print("fetchall:")
  result = cur.fetchall() 
  for r in result:
    print(r)
  con.close()
