FROM python:3.8

RUN pip3 install fastapi uvicorn

EXPOSE 8000

COPY main.py /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]