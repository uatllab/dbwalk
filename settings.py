#!/bin/env python

"""
jc 2025
"""

DEBUG = 0
HTTPIE_BIN = "/usr/bin/http"
URL = "https://intranet.uatl-eca.fr"

CSV_SEP = ";"
ENCODING_ERRORS = "replace"
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

CUR_YEAR = 2025

MEMBERSHIP_QUERY = 337
MEMBERSHIP_DATECOLS = [ "CreatedDateTime" ]
MEMBERSHIP_COLS = [
    'Status'
    , 'CreatedDateTime'
    # , 'ValidDateTime'
    # , 'InvoicedDateTime'
    # , 'Rate'
    # , 'SupportingDocumentsPortfolioId'
    # , 'PaymentType'
    # , 'AcceptImageRight'
    , 'Id'
    , 'MemberId'
    # , 'AcceptNewsletter'
    , 'Year_Code'
    # , 'AcceptYearReduction'
    ]

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

