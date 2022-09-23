import pandas as pd  
from sqlalchemy import create_engine  
from datetime import datetime
from io import StringIO

import pandas
import requests


def df_map(df, mapping):
    new_df = pandas.DataFrame()
    for key in mapping:
        new_df[key] = df[mapping[key]]
    return new_df

date_start = datetime(2021, 2, 3)
date_end = datetime(2021, 6, 24)
r = requests.get('http://quotes.money.163.com/service/chddata.html?code=' + ('%07d' % 1000031)
                     + '&start=' + date_start.strftime('%Y%m%d') + '&end=' + date_end.strftime('%Y%m%d'))
df = pandas.read_csv(StringIO(r.text))
df['股票代码'] = pandas.to_numeric(df['股票代码'].str.slice(1))
df2 = df_map(df, {'code': '股票代码','name':'名称', 'date': '日期', 'open': '开盘价', 'high': '最高价',
                       'low': '最低价', 'close': '收盘价', 'volume': '成交量', 'rate':'涨跌幅','turnover':'换手率',
                       'yest_close': '前收盘', 'price': '收盘价'})


yconnect = create_engine('mysql+mysqldb://root:root@localhost:3306/quantra?charset=utf8')
pd.io.sql.to_sql(df2,'stock_data', yconnect, schema='quantra',if_exists='append',index=False)  
