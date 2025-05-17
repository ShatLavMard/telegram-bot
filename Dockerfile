FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
python bot.py


CMD ["python", "bot.py"]

