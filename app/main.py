from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_stock_price_info():
    return {}
