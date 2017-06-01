import oandapy as opy
import loginkeys as login
from datetime import datetime, timedelta
from oandapyV20 import API
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.orders as orders

api = API(login.ACCESS_TOKEN)

# Retrieve Pricing Info
params = {
          "instruments": "EUR_USD,EUR_JPY"
        }
r = pricing.PricingInfo(accountID=login.ACCOUNT_ID, params=params)
rv = api.request(r)

# Create Order

orderbody = {
    "order": {
        "price": "1.2",
        "stopLossOnFill": {
          "timeInForce": "GTC",
          "price": "1.22"
        },
        "timeInForce": "GTC",
        "instrument": "EUR_USD",
        "units": "100",
        "type": "LIMIT",
        "positionFill": "DEFAULT"
      }
}
r = orders.OrderCreate(login.ACCOUNT_ID, data=orderbody)
api.request(r)
print r.response






# # Fetch Rates- EUR_USD
# response = oanda.get_prices(instruments = "EUR_USD")
# prices = response['prices']
# print prices
# bidding_price = float(prices[0]["bid"])
# ask_price = float(prices[0]["ask"])
# time = prices[0]["time"]
# instrument = prices[0]["instrument"]
#
#
# '''Send an order'''
#
# # set the trade to expire after one day
# trade_expire = datetime.now() + timedelta(days=1)
# trade_expire = trade_expire.isoformat("T") + "Z"
#
# order = oanda.create_order(login.account_id, instrument='EUR_USD', units=1000, side="buy", type='limit',
#                            price=1.12, expiry=trade_expire)
# print order
