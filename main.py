from fxtrade.broker.oanda import Oanda
from fxtrade.collections.instrument import instrumentCollection

if __name__ == '__main__':
    broker = Oanda()

    instrumentCollection.CreateFile(broker.get_account_instruments(), "./data")
    instrumentCollection.LoadInstruments("./data")
    instrumentCollection.PrintInstruments()
