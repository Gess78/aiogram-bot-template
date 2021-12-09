FROM python:3.9-slim

WORKDIR /usr/src/app/tg_bot

COPY requirements.txt /usr/src/app/tg_bot
RUN pip install -r /usr/src/app/tg_bot/requirements.txt
COPY . /usr/src/app/tg_bot

CMD python3 -m bot