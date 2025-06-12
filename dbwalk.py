#!/bin/env python

"""
jc 2025
"""

import os
import pandas as pd
from abc import ABC, abstractmethod
import secret
import settings as cf


def log(level,msg):
    if level<=cf.DEBUG:
        print(f"log{level}: {msg}")

class Session:

  def open(self,user=secret.SESSION_LOGIN, pwd=secret.SESSION_PASSWD, session="mysession"):
    self.session = session
    f_out = f"/tmp/{self.session}_open" 
    cmd = f"{cf.HTTPIE_BIN} -I --session={session} -f POST {cf.URL}/Account/LogOn UserName={user} Password={pwd} > {f_out}"
    log(1,f"{cmd=}")
    return os.system(cmd)

  def query(self,id):
    f_out = f"/tmp/{self.session}_query{id}"
    cmd = f"{cf.HTTPIE_BIN} -I --session={self.session} {cf.URL}/Query/ExecuteQuery/{id} | tail -n +2 > {f_out}"
    cmd = f"{cf.HTTPIE_BIN} -I --session={self.session} {cf.URL}/Query/ExecuteQuery/{id} > {f_out}"
    log(1,f"{cmd=}")
    os.system(cmd)
    return f_out

class BaseTable(ABC):
    def __init__(self,file,datecols=[]):
        df = pd.read_csv(
            file
            , sep=cf.CSV_SEP
            , encoding_errors=cf.ENCODING_ERRORS
            , parse_dates=datecols
            , date_format= { x:cf.DATE_FORMAT for x in datecols }
            )

        self.df = df
        self.datecols = datecols

    def colnames(self):
        return list(self.df.columns)

    @abstractmethod
    def adjust(self):
        pass

    def __str__(self):
        return str(self.df)

class MembershipTable(BaseTable):
    def __init__(self,file,datecols=cf.MEMBERSHIP_DATECOLS):
        super().__init__(file,datecols)

    def adjust(self):
        df = self.df
        df['year'] = pd.DatetimeIndex(df['CreatedDateTime']).year
        df = df.loc[df["year"] == cf.CUR_YEAR, cf.MEMBERSHIP_COLS ]
        self.df = df

class WishTable(BaseTable):
    def __init__(self,file,datecols=cf.WISH_DATECOLS):
        super().__init__(file,datecols)

    def adjust(self):
        df = self.df
        df['year'] = pd.DatetimeIndex(df['Date']).year
        df = df.loc[df["year"] == cf.CUR_YEAR, cf.WISH_COLS ]
        self.df = df

if __name__ == "__main__":
  session = Session()
  session.open(user=secret.SESSION_LOGIN, pwd=secret.SESSION_PASSWD)  

  membership_query = session.query(cf.MEMBERSHIP_QUERY)   
  mt = MembershipTable(membership_query)
  mt.adjust()
  print(mt.colnames())
  print(mt)

#   wish_query = session.query(cf.WISH_QUERY)   
#   wt = WishTable(wish_query)
#   wt.adjust()
#   print(wt)