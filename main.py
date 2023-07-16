import httpx
import xmltodict
import json
from fastapi import FastAPI

app = FastAPI()

URL = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"
PARAM1 = "serviceKey"
KEY1 = ""
PARAM2 = "itmsNm"
KEY2 = "카카오"


@app.get("/")
async def get_stock_price_info():
    raw_response = httpx.get(URL, params={PARAM1: KEY1, PARAM2: KEY2})
    response = json.dumps(xmltodict.parse(raw_response.text))
    print(response)
    return response
