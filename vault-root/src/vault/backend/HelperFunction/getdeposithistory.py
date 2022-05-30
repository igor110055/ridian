# standard library:
import requests
from requests import Request, Session
import hmac
import datetime

def get_deposit_history():
        resp = requests.get('https://otc.ftx.com/api/time')
        ftx_t = resp.json()
        time = ftx_t['result']
        date_format = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
        unix_time = datetime.datetime.timestamp(date_format)
        ts = unix_time*1000
        deposits = Request(
                    "GET", "https://ftx.com/api/wallet/deposits")
        deposits_url = deposits.prepare()
        signature_payload = f"{ts}{deposits_url.method}{deposits_url.path_url}".encode(
                )
                  
        signature = hmac.new("IUw47_jaWULymqs-gZd2udPUYYQq1_n76V8bwJsm".encode(),
        signature_payload, "sha256").hexdigest()
        deposits_url.headers["FTX-KEY"] = "szi72POBX0TH086Gebtut76pKUC7vVAPnM2QUf0X"
        deposits_url.headers["FTX-SIGN"] = signature
        deposits_url.headers["FTX-TS"] = str(ts)\
        
        return deposits_url