FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY weather-info.py .

ENTRYPOINT [ "python", "weather-info.py" ]
