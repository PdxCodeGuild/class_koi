# Rain Data
# Version 1
# Mitch Chapman

#################
################
############### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##############
############# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
############  This code does not run as expected. I am leaving it here for now.
############# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##############
############### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
################
#################



import datetime
from email.utils import parsedate, parsedate_to_datetime
import pandas


def dd_mmm_yyyy_parser(date):
    return datetime.datetime.strptime(date, '%d-%m-%Y')
#  parse_dates=['Date'], date_parser=dd_mmm_yyyy_parser


url = "https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain"
df = pandas.read_fwf(url, skiprows=(0,1,2,3,4,5,6,7,8,10), headers=None, parse_date=["Date"], date_parser=dd_mmm_yyyy_parser, dayfirst=True)

df1 = df.groupby(["Date", "Total"]).mean()

print(df1)









