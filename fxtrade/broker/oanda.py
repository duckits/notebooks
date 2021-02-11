import os
import requests

class Oanda:

  def __init__(self):
    self.account_id = os.getenv('OANDA_ACCOUNT_ID')
    self.api_key = os.getenv('OANDA_API_KEY')
    self.session = requests.Session()
    self.session.headers.update({
      "Authorization": f"Bearer {self.api_key}",
      "Content-Type": "application/json"
    })
    self.url = os.getenv('OANDA_API_URL')

  def request(self, url, verb='get', params=None, data=None, headers=None):
    full_url = f"{self.url}/{url}"
    try:
      response = None
      if verb == "get":
        response = self.session.get(full_url, params=params, data=data, headers=headers)

      if response == None:
        return False, {'error': 'verb not found'}

      return response.json()

    except Exception as error:
      return False, {'Exception': error}

  def get_accounts(self):
    data = self.request("accounts")
    return data['accounts']

  def get_account_summary(self):
    data = self.request(f"accounts/{self.account_id}/summary")
    return data['account']

  def get_account_instruments(self):
    data = self.request(f"accounts/{self.account_id}/instruments")
    return data['instruments']

  def get_instrument_candles(self, instrument, params):
    data = self.request(f"instruments/{instrument}/candles", params=params)
    return data

