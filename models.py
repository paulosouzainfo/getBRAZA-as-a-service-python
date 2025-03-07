from pydantic import BaseModel

class PixSchema(BaseModel):
    url_callback: str
    amount: str
    markup_type: str = "N"
    markup_value: str = "0"
    pair: str = "USDTBRL"
    coin: str = "USDT"

class WithdrawSchema(BaseModel):
    wallet: str
    amount: str
    coin: str = "USDT"
    blockchain: str = "TRON"

class TransferSchema(BaseModel):
    to_account_number: str
    coin_name: str = "USDT"
    amount: float