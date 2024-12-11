# Goal

A bot to auto-detect if some on have a send-money post in PTT, and auto send reply in the article by users account

# Usage

### brief explanation

There are 3 ways to start the code.

- Python
- Docker
- Docker compose

### Python

- Install Python, Python version have higher than 3.10.
- Install requirements

```shell
pip install -r requirements.txt
```

- run python

```shell
python --account <PTT account> --password <PTT password>
```

### Docker

- Install docker
- run the command

```shell
 docker run -it -e ACCOUNT=<PTT account> -e PASSWORD=<PTT password> markliuliu/ptt_money_collector:1.0.3
```

### Docker container (recommend)

- Install docker
- write file named as `.env` under `PttMoneyCollector`.

```
ACCOUNT=<PTT account>
PASSWORD=<PTT password>
```

- run the command

```shell
docker-compose up
```
