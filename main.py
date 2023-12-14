import requests
from fastapi import FastAPI
from Scrapper import Scrapper
app = FastAPI()

@app.get('/{stock}')
def getprice(stock: str):
    stock = Scrapper(stock)
    return stock.getPrice()
