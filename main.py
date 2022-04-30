# main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    element: str

class Calculator(BaseModel):
    expr: str

elements = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sum1n/{number}")
async def sum_to_n(number: int):
    sum = 0
    for i in range(1,number+1):
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

@app.put("/list")
async def update_list(item: Item):
    elements.append(item.element)
    return {"result": item.element}

@app.get("/list")
async def get_list():
    return {"result": elements}

@app.post("/calculator")
async def calculator(calculator: Calculator):
    expr = calculator.expr
    arr = expr.split(',')
    num1 = int(arr[0])
    num2 = int(arr[2])
    op = arr[1] # arithmetic operation
    result = -1
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return {"error": "zerodiv"}
        result = int(num1 / num2)
    else:
        return {"error": "invalid"}
    
    return {"result": result}
    