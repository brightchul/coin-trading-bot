# coin-trader-bot

```bash
# poetry가 설치되어 있어야 합니다.
$ git clone https://github.com/brightchul/coin-trading-bot.git
cd coin-trading-bot

# 의존성 설치
poetry install

# venv 실행
poetry shell



# poetry shell 를 하게 되면 새로운 하위 셀이 생성되기 때문에 경로가 ~로 이동합니다.
# 다시 설치된 경로로 돌아와서 작업을 시작합니다. 
cd ./디렉토리/coin-trading-bot

# .env_sample을 복사해서 .env를 생성하고 bithumb 키와 시크릿을 넣습니다. 
cp .env_sample .env


python run.py
```