# explorations of NJ SR1A data in hoboken with pandas numpy and ipython
# Anthony Townsend
# 26 feb 2016

# imports Hoboken 2x file -- all Hoboken properties sold twice
import pandas as pd
import numpy as np
df = pd.read_csv('hoboken_2x.csv', header=0, index_col='pams_pin')
df[:5]
df.describe(reported_sales_price)
df['reported_sales_price'].describe()
#

## connect dataframe from psql
from sqlalchemy import create_engine
engine = create_engine('postgresql://user@localhost:5432/parcels')

# fetch full sr1a (takes a looong time, probably dies)
sr1a = pd.read_sql_query('select * from "sr1a"',con=engine)

# just the hoboken records
hoboken = pd.read_sql_query('select * INTO hoboken_sr1a from 'sr1a' where county_code=09 AND district_code=05',con=engine)


copy sr1a to '/Users/anthonytownsend/Desktop/Code/parcels/nj/working/hb_sr1a.csv' delimiter ',' csv header;