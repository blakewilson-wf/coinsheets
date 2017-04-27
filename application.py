import urllib2
import time

from coinbase.wallet.client import Client as CoinbaseClient
from pyclient.swagger_client.apis.spreadsheets_api import SpreadsheetsApi
from pyclient.swagger_client.api_client import ApiClient
from pyclient.swagger_client.configuration import Configuration

api_client = ApiClient()
Configuration().access_token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IlQwRjFkR2d5TUZSdmEyVnVTMlY1VUdGeVpXNTBIazlCZFhSb01qQlViMnRsYmt0bGVVbEVIazlCZFhSb01qQlViMnRsYmt0bGVSODFOekEzTnpBeU1qazROek00TmpnNCJ9.eyJtcmlkIjoiVFdWdFltVnljMmhwY0I4Mk1qQTNNelUyTlRFek9ERXlORGd3IiwibWVtIjo2MjA3MzU2NTEzODEyNDgwLCJyb2xlcyI6W10sInNjb3BlIjoiZGF0YV90YWJsZXN8ciBkYXRhX3RhYmxlc3x3IiwibGljZW5zZXMiOltdLCJzY3AiOlsiZGF0YV90YWJsZXN8ciIsImRhdGFfdGFibGVzfHciXSwiYWNjIjo1NjM5NDQ1NjA0NzI4ODMyLCJwYXIiOiI3YjYzYjk5OWIzMzE0ZjEwOTM1YWQ2NTc2NTUxZGE3MyIsInZlciI6NCwiYXVkIjoiODE2NmE1MTNhMmJkNGU1ODgxNmViYTgzOWQ0YzljZGMiLCJnbnQiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJjaWQiOiI4MTY2YTUxM2EyYmQ0ZTU4ODE2ZWJhODM5ZDRjOWNkYyIsImlzcyI6Imh0dHBzOi8vd2stZGV2LndkZXNrLm9yZyIsIndzayI6MCwiYXJpZCI6IlFXTmpiM1Z1ZEI4MU5qTTVORFExTmpBME56STRPRE15IiwianRpIjoiYzk3ODlmMzM4ZDYwNDFkYmE2NzJmNTkyOWQzMWZiMmYiLCJ1c3IiOjQ4NDgwMzcyMTQwMjc3NzYsImV4cCI6MTQ5MzMxNTg2MywiaWF0IjoxNDkzMzE1MjYzLCJ1cmlkIjoiVjBaVmMyVnlIelE0TkRnd016Y3lNVFF3TWpjM056WSJ9.w3DKsUsAlH84MxFdxTc8gZebnR4ez1LcOHqATsbcxokxlwoMZ69TLfi2nl-inIL_Gcwz6epcLce0c1TYNBvMrj_lYwmeOJOathRAm6IyDs4mac3uvLd4JPtvPNuB7thdlGAuz9UxB9RsjwVFKmpQIdBtG5rRZQPmqDOCKaepvIXar3sGAVGFN4ufAMQVDOO2GNoyFWH9egW51Ik9mti2BaKs62BTGBntGuSoGc67ISbuoCyGpx_2h9E3B9ijsSCecTvASywlXNSBavcsmOttV5Kj4XZu1yNdUhXRUWJ6HI6sy8kRZSoFmeGkoe199ScL6UB29oDpUjSd4-4am8U6CQ'
spreadsheets_client = SpreadsheetsApi()


class Client:

    def __init__(self):
        self.coinbase_client = CoinbaseClient('kjbqArvnGOKiVsCL', '1EtHiISTUavVa5CxqUpKIxi2bmEddW2N')
        self.currency_code = 'USD'  # can also use EUR, CAD, etc.
        self.sp_api_client = SpreadsheetsApi()

    def set_price_in_sheet(self):
        while True:
            time.sleep(5)

            # Make the request
            price = self.coinbase_client.get_spot_price(currency=self.currency_code)

            print 'Current bitcoin price in %s: %s' % (self.currency_code, price.amount)

            # Update the Spreadsheet
            resp = spreadsheets_client.spreadsheets_spreadsheet_id_sheets_sheet_id_data_put('067474f68bcc4fada0da5b85fe9b6b62',
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
