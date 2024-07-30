
FROM python:3.12

WORKDIR /app/

# Prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to the terminal without buffering
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/entrypoint.sh

COPY . /app/

ENTRYPOINT [ "/app/entrypoint.sh" ]