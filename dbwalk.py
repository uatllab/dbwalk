#!/bin/env python

"""
jc 2025
"""

import os
import pandas as pd
from abc import ABC, abstractmethod
import secret

DEBUG = 0
HTTPIE_BIN = "/usr/bin/http"
URL = "https://intranet.uatl-eca.fr"

CSV_SEP = ";"
ENCODING_ERRORS = "replace"
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

CUR_YEAR = 2025

WISH_QUERY = 336
WISH_DATECOLS = [ "Date" ]
WISH_COLS = [
                'Id'
                , 'Order'
                , 'Status'
                , 'Date'
                , 'MembershipId'
                , 'ActivityId'
                , 'ProcessStatus'
                , 'RandomTIV'
                , 'year'
            ]

def log(level,msg):
    if level<=DEBUG:
        print(f"log{level}: {msg}")

class Session:

  def open(self,user=secret.SESSION_LOGIN, pwd=secret.SESSION_PASSWD, session="mysession"):
    self.session = session
    f_out = f"/tmp/{self.session}_open" 
    cmd = f"{HTTPIE_BIN} -I --session={session} -f POST {URL}/Account/LogOn UserName={user} Password={pwd} > {f_out}"
    log(1,f"{cmd=}")
    os.system(cmd)

  def query(self,id):
    f_out = f"/tmp/{self.session}_query{id}"
    cmd = f"{HTTPIE_BIN} -I --session={self.session} {URL}/Query/ExecuteQuery/{id} | tail -n +2 > {f_out}"
    cmd = f"{HTTPIE_BIN} -I --session={self.session} {URL}/Query/ExecuteQuery/{id} > {f_out}"
    log(1,f"{cmd=}")
    os.system(cmd)
    return f_out

class BaseTable(ABC):
    def __init__(self,file,datecols=[]):
        df = pd.read_csv(
            file
            , sep=CSV_SEP
            , encoding_errors=ENCODING_ERRORS
            , parse_dates=datecols
            , date_format= { x:DATE_FORMAT for x in datecols }
            )

        self.df = df
        self.datecols = datecols

    def colnames(self):
        return list(t.df.columns)

    @abstractmethod
    def adjust(self):
        pass

    def __str__(self):
        return str(self.df)

class WishTable(BaseTable):
    def __init__(self,file,datecols=WISH_DATECOLS):
        super().__init__(file,datecols)

    def adjust(self):
        df = self.df
        df['year'] = pd.DatetimeIndex(df['Date']).year
        df = df.loc[df["year"] == CUR_YEAR, WISH_COLS ]
        self.df = df

if __name__ == "__main__":
  session = Session()
  session.open()  
  wish_query = session.query(WISH_QUERY)   
  wt = WishTable(wish_query)
  wt.adjust()
  print(wt)