#!/bin/env python

"""
jc 2025
"""

DEBUG = 0
HTTPIE_BIN = "/usr/bin/http"
TMPDIR = "/tmp"

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

ACTIVITY_QUERY = 338
ACTIVITY_DATECOLS = [ "StartDate", "EndDate" ]
ACTIVITY_COLS = [
    
         "Id"
        , "Reference"
        , "Label"
        , "Cycle"
        , "LeaningCycleYear"
        , "Description"
        , "LevelDescription"
        , "FrequencyDay"
        , "FrequencyStartHour"
        , "FrequencyEndHour"
        , "AvalaiblePlacesCount"
        , "SpecificParticipation"
        , "Filmed"
        , "VideoLink"
        , "StartDate"
        , "EndDate"
        , "RoomConfiguration"
        , "EquipmentRequest"
        , "SpecificParticipationPortfolioId"
        , "SpecificParticipationDecision"
        , "NeedFinanceDescription"
        , "NeedFinancePortfolioId"
        , "NeedFinanceDecision"
        , "StopDate"
        , "StopDateReason"
        , "Level"
        , "CalendarId"
        , "AnimatorSecurityGroupId"
        , "MemberSecurityGroupId"
        , "RoomCode"
        , "MainPortfolioId"
        , "Year_Code"
        , "ActivityCategory_Code"
        , "ParentId"
        , "IsArchived"
        , "IFrameVideoLink"
        , "NeedFinanceFormation"
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

