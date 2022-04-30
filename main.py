# main.py

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sum1n/{number}")
async def sum_to_n(number: int):
    sum = 0
    for i in range(1,number):
        sum = sum + i
    return {"result": sum}


@app.get("/fibo/")
async def fibonacci(n: int):
    num1 = 0
    num2 = 1
    result = num1+num2
    num1=num2
    num2=result
    count=0
    for i in range(2, n):
        result = num1+num2
        num1=num2
        num2=result
    return {"result": num1}


@app.post("/reverse")
async def reverse(request: Request):
    string = request.headers.get('string')
    return {"result": string[::-1]}
