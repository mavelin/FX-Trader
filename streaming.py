import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import loginkeys as login
import json

accountID = login.ACCOUNT_ID
accessToken = login.ACCESS_TOKEN
api = API(access_token=accessToken)
params = {
    "instruments": "EUR_USD"
}

r = pricing.PricingStream(accountID=accountID, params=params)
rv = api.request(r)

maxrecs = 100
for ticks in rv:
    print json.dumps(ticks, indent=4), ","
    if maxrecs == 0:
        r.terminate("maxrecs records received")
