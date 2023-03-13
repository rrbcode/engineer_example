import json
import datetime
from tempfile import NamedTemporaryFile
from typing import List
import boto3


from api import MercadoBitcoinApi

class S3Writer:
    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.tempfile = NamedTemporaryFile()
        self.key = f"mercado_bitcoin/day-summary/coin={self.coin}/extracted_at={datetime.datetime.now().date()}/{datetime.datetime.now()}.json"
        self.s3 = boto3.client("s3")

    def _write_to_file(self, data: [List, dict]):
        with open(self.tempfile.name, "a") as f:
            f.write(json.dumps(data) + "\n")

    def _write_file_to_s3(self):
        self.s3.put_object(
            Body=self.tempfile,
            Bucket="mercado-bitcoin-bucket",
            Key=self.key
        )

    def write(self, data: [List, dict]):
        self._write_to_file(data=data)
        self._write_file_to_s3()

def handler(event, context):
    coin = "BTC"
    date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    api = MercadoBitcoinApi(coin=coin)
    data = api.get_data(date=date)

    writer = S3Writer(coin=coin)
    writer.write(data)