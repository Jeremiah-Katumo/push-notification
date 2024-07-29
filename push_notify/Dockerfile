
FROM python:3.11.9

WORKDIR /app/

# Prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to the terminal without buffering
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt --nocache-dir

COPY entrypoint.sh /app/entrypoint.sh

COPY . /app/

ENTRYPOINT [ "/app/entrypoint.sh" ]