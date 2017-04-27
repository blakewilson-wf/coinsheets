import time
import threading

from coinbase.wallet.client import Client as CoinbaseClient
from pyclient.swagger_client.apis.authentication_api import AuthenticationApi
from pyclient.swagger_client.apis.spreadsheets_api import SpreadsheetsApi
from pyclient.swagger_client.configuration import Configuration

import requests
import json


class Client:

    def __init__(self):
        self.coinbase_client = CoinbaseClient('kjbqArvnGOKiVsCL', '1EtHiISTUavVa5CxqUpKIxi2bmEddW2N')
        self.currency_code = 'USD'  # can also use EUR, CAD, etc.
        self.sp_api_client = SpreadsheetsApi()
        self.auth_api_client = AuthenticationApi()
        self._set_token()
        self.wb = '067474f68bcc4fada0da5b85fe9b6b62'
        self.tb = 'a47eddaf73b64709a2db2d893e3dfddd'

    def _set_token(self):
        Configuration().access_token = self.auth_api_client.oauth2_token_post(client_id='04fffc2536fa4978808ac680dbbecacc',
                                                                              x_api_key='',
                                                                              client_secret='4e8ecf9b8d20504352b7539dc0a664095ed52a80ff8517a0',
                                                                              grant_type='client_credentials').access_token
        # Renew token every minute
        t = threading.Timer(60.0, self._set_token)
        t.daemon = True
        t.start()

    def set_price_in_sheet(self):
        # Make the request
        btc_price = self.coinbase_client.get_spot_price(currency_pair='BTC-USD')
        self.coinbase_client.get_historic_prices()
        resp = requests.get(url='https://api.coinbase.com/v2/prices/ETH-USD/spot', headers={'Authorization': 'Bearer ' + Configuration().access_token})
        eth = json.loads(resp.text)
        eth_price = eth['data']['amount']

        # Update the Spreadsheet
        resp = self.sp_api_client.spreadsheets_spreadsheet_id_sheets_sheet_id_data_put('067474f68bcc4fada0da5b85fe9b6b62',
            'a47eddaf73b64709a2db2d893e3dfddd',
            {
                "values": [
                    [
                    "Bitcoin price (in dollars)",
                    btc_price.amount
                    ],
                    ["ETH price (in dollars)",
                        eth_price]
                ]
            }, 'fakekey',
            region='A1:B2',)


    def set_exchange_rates_in_sheet(self):
        while True:
            raw_input("Press 'Enter' to refresh exchange rates")
            rates = self.coinbase_client.get_exchange_rates(currency="BTC")
            values = [["BTC Exchange Rates", ""]]
            for k, v in rates["rates"].iteritems():
                values.append([k, v])
            # Update the Spreadsheet
            resp = self.sp_api_client.spreadsheets_spreadsheet_id_sheets_sheet_id_data_put('067474f68bcc4fada0da5b85fe9b6b62',
                'a47eddaf73b64709a2db2d893e3dfddd',
                {
                    "values":
                        values
                }, 'fakekey',
                region='A4:B',)

if __name__ == "__main__":
    c = Client()
    thr = threading.Thread(target=c.set_price_in_sheet, kwargs={})
    thr.start()
    thr = threading.Thread(target=c.set_exchange_rates_in_sheet, kwargs={})
    thr.start()
