
FROM python:3.11.9

WORKDIR /app/

COPY requirements.txt .

COPY endpoint.sh .

RUN pip install -r requirements.txt --nocache-dir

