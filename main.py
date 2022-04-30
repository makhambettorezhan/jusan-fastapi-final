# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sum1n/{number}")
async def sum_to_n(number: int):
    sum = 0
    for i in range(1,number):
        sum = sum + i
    return {"message": f"The sum from 1 to {number} is {sum}"}