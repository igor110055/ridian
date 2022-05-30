# standard library:
import requests
from requests import Request, Session
import hmac
import datetime

def transaction(amount,coin,address,api_key,secrets_key):
        resp = requests.get('https://otc.ftx.com/api/time')
        ftx_t = resp.json()
        time = ftx_t['result']
        date_format = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
        unix_time = datetime.datetime.timestamp(date_format)
        ts = unix_time*1000
        
        body = {
            "coin": coin,
            "size":amount,
            "address": address,
            "method": "matic",
             }

        withdrawals_request = Request(
            'POST', 'https://ftx.com/api/wallet/withdrawals',  json=body)
        prepared = withdrawals_request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode(
        )
        if prepared.body:
            signature_payload += prepared.body

        signature_payload = signature_payload
        signature = hmac.new(secrets_key.encode(),
                             signature_payload, 'sha256').hexdigest()

        prepared.headers['FTX-KEY'] = api_key
        prepared.headers['FTX-SIGN'] = signature
        prepared.headers['FTX-TS'] = str(ts)
        
        
        return prepared