import bridge
from fastapi import FastAPI
from pydantic import BaseModel

class TradingviewSignal(BaseModel):
    action: str
    contracts: str
    marketPosition: str
    positionSize: str
    prevMarketPosition: str
    price: str
    symbol: str
    time: str

app = FastAPI()

@app.post("/tradingview-signal/9781f744-9bc1-49da-9f11-75b654dd888f")
def handle_signal(signal: TradingviewSignal):
    if signal.action == 'buy':
        bridge.open_long()
    elif signal.action == 'sell':
        bridge.close_long()
    else:
        print('Unknown action from tradingview.')
