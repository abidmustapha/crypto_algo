# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:42:36 2024

@author: ABID
"""


KLINE_INTERVAL_1SECOND = "1s"
KLINE_INTERVAL_1MINUTE = "1m"
KLINE_INTERVAL_3MINUTE = "3m"
KLINE_INTERVAL_5MINUTE = "5m"
KLINE_INTERVAL_15MINUTE = "15m"
KLINE_INTERVAL_30MINUTE = "30m"
KLINE_INTERVAL_1HOUR = "1h"
KLINE_INTERVAL_2HOUR = "2h"
KLINE_INTERVAL_4HOUR = "4h"
KLINE_INTERVAL_6HOUR = "6h"
KLINE_INTERVAL_8HOUR = "8h"
KLINE_INTERVAL_12HOUR = "12h"
KLINE_INTERVAL_1DAY = "1d"
KLINE_INTERVAL_3DAY = "3d"
KLINE_INTERVAL_1WEEK = "1w"
KLINE_INTERVAL_1MONTH = "1M"



#timeframe = int(dt.datetime(2021, 4, 1, 1, 0, 0).timestamp() * 1000 - dt.datetime(2021, 4, 1, 0, 0, 0).timestamp() * 1000)
# klines = []
# symbol_existed = False
# temp_starttime = int(dt.datetime(2021, 4, 1).timestamp() * 1000)
# while True:
#     temp_klines = client.get_klines(symbol=my_symbol, interval=my_interval, limit=my_limit, startTime=temp_starttime)
#     if not symbol_existed and len(temp_klines):
#         symbol_existed = True
#     if symbol_existed:
#         klines += temp_klines
#         temp_starttime = temp_klines[len(temp_klines) - 1][0] + timeframe
#     else:
#         temp_starttime =  timeframe
    
#     if len(temp_klines) < my_limit:
#         break

# df_klines = pd.DataFrame(klines)


#dt.timedelta(0, 1)