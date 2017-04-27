import urllib2
import time
from threading import Timer

from coinbase.wallet.client import Client as CoinbaseClient
from pyclient.swagger_client.apis.authentication_api import AuthenticationApi
from pyclient.swagger_client.apis.spreadsheets_api import SpreadsheetsApi
from pyclient.swagger_client.configuration import Configuration


class Client:

    def __init__(self):
        self.coinbase_client = CoinbaseClient('kjbqArvnGOKiVsCL', '1EtHiISTUavVa5CxqUpKIxi2bmEddW2N')
        self.currency_code = 'USD'  # can also use EUR, CAD, etc.
        self.sp_api_client = SpreadsheetsApi()
        self.auth_api_client = AuthenticationApi()
        self._set_token()

    def _set_token(self):
        Configuration().access_token = self.auth_api_client.oauth2_token_post(client_id='04fffc2536fa4978808ac680dbbecacc',
                                                                              x_api_key='',
                                                                              client_secret='4e8ecf9b8d20504352b7539dc0a664095ed52a80ff8517a0',
                                                                              grant_type='client_credentials').access_token
        # Renew token every minute
        t = Timer(60.0, self._set_token)
        t.daemon = True
        t.start()

    def set_price_in_sheet(self):
        while True:
            time.sleep(5)

            # Make the request
            price = self.coinbase_client.get_spot_price(currency=self.currency_code)

            print 'Current bitcoin price in %s: %s' % (self.currency_code, price.amount)

            # Update the Spreadsheet
            resp = self.sp_api_client.spreadsheets_spreadsheet_id_sheets_sheet_id_data_put('067474f68bcc4fada0da5b85fe9b6b62',
                'a47eddaf73b64709a2db2d893e3dfddd',
                {
                    "values": [
                        [
                        "Bitcoin price (in dollars)",
                        price.amount
                        ],
                    ]
                }, 'fakekey')

            print(str(resp))

if __name__ == "__main__":
    c = Client()
    c.set_price_in_sheet()
