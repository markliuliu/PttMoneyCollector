FROM python:3.12-slim

WORKDIR /code
ADD ./src /code/src
ADD ./requirements.txt /code
RUN pip install -r requirements.txt

ADD ./start_ptt_money_collector.sh /code
RUN chmod +x ./start_ptt_money_collector.sh

ENV TZ=Asia/Taipei

