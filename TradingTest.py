import oandapy as opy
import loginkeys as login
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()  # 18


oanda = opy.API(environment='practice',
                access_token=login.access_token)

data = oanda.get_history(instrument='EUR_USD',  # our instrument
                         start='2016-12-08',  # start data
                         end='2016-12-10',  # end date
                         granularity='M1')  # minute bars  # 7

df = pd.DataFrame(data['candles']).set_index('time')  # 8

df.index = pd.DatetimeIndex(df.index)  # 9

df.info() # 10

df['returns'] = np.log(df['closeAsk'] / df['closeAsk'].shift(1))  # 12

cols = []  # 13

for momentum in [15, 30, 60, 120]:  # 14
    col = 'position_%s' % momentum  # 15
    df[col] = np.sign(df['returns'].rolling(momentum).mean())  # 16
    cols.append(col)  # 17

strats = ['returns']  # 19

for col in cols:  # 20
    strat = 'strategy_%s' % col.split('_')[1]  # 21
    df[strat] = df[col].shift(1) * df['returns']  # 22
    strats.append(strat)  # 23

df[strats].dropna().cumsum().apply(np.exp).plot()  # 24

# # Get Price for Instrument
# response = oanda.get_prices(instruments="EUR_USD")
# prices = response.get("prices")
# asking_price = prices[0].get("ask")



# # Streaming
# class MyStreamer(opy.Streamer):
#     def __init__(self, count=10, *args, **kwargs):
#         super(MyStreamer, self).__init__(*args, **kwargs)
#         self.count = count
#         self.reccnt = 0
#
#     def on_success(self, data):
#         print data, "\n"
#         self.reccnt += 1
#         if self.reccnt == self.count:
#             self.disconnect()
#
#     def on_error(self, data):
#         self.disconnect()
#
#
# stream = MyStreamer(environment="practice", access_token=login.access_token)
# stream.rates(login.account_id, instruments="EUR_USD,EUR_JPY,US30_USD,DE30_EUR")
#
