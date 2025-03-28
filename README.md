# TODO: попробовать генерацию кода с помощью openapi https://github.com/openapi-generators/openapi-python-client

# fastapi-template

- All libraries should be async

# See this if you are looking for tools

- https://github.com/zhanymkanov/fastapi-best-practices

# Real production ready projects

- https://github.com/polarsource/polar # Good UI on next JS
- https://github.com/Netflix/dispatch # Vue UI, RBAC
- https://github.com/TracecatHQ/tracecat
- https://github.com/ljvmiranda921/sprites-as-a-service  # Vue

# Examples and read projects

- https://github.com/fastapi/full-stack-fastapi-template # From fastapi devs
- https://github.com/codewitgabi/full-featured-social-media-application-fastapi # RBAC, SSE
- https://github.com/denisxab/fastapi-accelerator

- https://github.com/fastapi-users/fastapi-users/tree/master
- https://github.com/arthurhenrique/cookiecutter-fastapi

# Load Tests / Metrics / Performance

- https://github.com/antonputra/tutorials/tree/251/lessons/239/fastapi-app





https://habr.com/ru/articles/816355/
Для python существует множество библиотек, предоставляющих различные реализации DI Container, я просмотрел почти все из них и записал лучшие IMO

python-dependency-injector - автоматизирован, основан на классах, имеет различные варианты жизненного цикла, такие как Singleton или Factory
lagom - интерфейс словаря с автоматическим разрешением
dishka - хороший контроль области видимости через менеджер контекста
that-depends - поддержка контекстных менеджеров (объекты должны быть закрыты в конце), встроенная интеграция fastapi
punq - более классический подход с методами register и resolve.
rodi - классический, простой, автоматический

# Попробовать в слоистой архиректуре собрать

- https://github.com/jujumilk3/fastapi-clean-architecture/tree/main/app/services
- https://github.com/0xTheProDev/fastapi-clean-example
- https://github.com/jujumilk3/fastapi-clean-architecture
- https://github.com/zhanymkanov/fastapi-best-practices
- https://github.com/fastapi-practices/fastapi_best_architecture
- https://www.youtube.com/watch?v=aF5_niKPL6c&ab_channel=UlbiTV

- https://github.com/jonra1993/fastapi-alembic-sqlmodel-async
- https://github.com/Youngestdev/fastapi-mongo/blob/master/tests/test_mock_database.py

# best practice

- Луковая архитектура
  - https://habr.com/ru/articles/672328/
- Анемичная модель предметной области (Anemic domain model)
- Паттерн репозиторий
- Депендерси индженкшен

- https://github.com/zhanymkanov/fastapi-best-practices

# Структура папок

Есть опции

- Групировка по домену
- Группировка по слоям

### внешний слой = infrastructure

api = controllers = http_clients = view
repositories = dao = data access = crud
configs

data transmit - dto - schema

services = bussiness logic = application services = service + impl
repositories = dao = interfaces = мапперы к и от доменной модели

domain = entities = core = model

adapters = interfaces = порты ?

# Запустить в виртуалке, она вообще потянет?

EasyOCR

# Auto Switch Server Bot

Auto Switch Server Bot is a Python application that automates the process of switching servers in a game using OCR (Optical Character Recognition) and keyboard/mouse automation. The application provides both a REST API and a CLI for interacting with the bot.

## Features

- Start the game through Steam
- Join a server by name
- OCR-based text recognition and interaction
- REST API using FastAPI
- CLI using Typer

## Installation

1. Clone the repository:

```bash
$ git clone https://github.com/yourusername/auto-switch-server-bot.git
$ cd auto-switch-server-bot
```

2. Install dependencies using `uv`:

```bash
$ uv sync
```

3. Activate the virtual environment:

```bash
$ .\.venv\Scripts\activate
```

## Usage

### Running the API

To run the FastAPI server:

```bash
$ uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Using the CLI

To use the CLI, run the following commands:

```bash
$ python -m app.interfaces.cli.cli_app start-game
$ python -m app.interfaces.cli.cli_app join-server
```

## Configuration

Configuration settings can be found in `app/configs/settings.py`. You can override these settings using environment variables with the prefix `APP_`.

## Logging

Logging configuration can be found in `app/utils/logging_config.py`. Logs are written to both the console and a rotating file `app.log`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

### Docs

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

### Get screenshot

```bash
uv run .\screen.py
```

### Code style

```bash
# use `uv run COMMAND` or activate env
ruff check
ruff check --select I --fix
ruff format





# Технологии брать которые на рынке сейчас популярней и дороже!
# Каталог паттернов https://martinfowler.com/eaaCatalog/

```bash
# dev
poetry shell
docker compose up db db-nosql -d
docker ps -a
docker stats
# run add in console or ide
# OR `uv run start`  # Check pyproject.toml
```

## Где остановился
- ёще раз глануть как реализован подход https://github.com/artemonsh/fastapi-onion-architecture/tree/pt2_unit_of_work/src

- https://fastapi.tiangolo.com/ru/tutorial/body/
- https://docs.pydantic.dev/latest/
- Реализовать работу с yookassa
- Разобраться с зависимостями https://pypi.org/project/dependencies/ для чего библа?
- Разобрать с тестами (изоляция бд, смотри примеры в github)

- принты на логи заменить

- настроить middleware (cors) и как быть с бекенд запросами, корс только на фронт?

  [//]: # (- Попробовать mongo подключить)
- Доделать интеграцию с mongo  # Подключить через ODM https://beanie-odm.dev/ или https://art049.github.io/odmantic/
- Попробовать подключить бесплатный кластер от cloud.mongodb.com (Atlas)
- Настроить реплики и шардирование БД

- настроить аутентификацию (jwt?)
- настроить метрики (prometheus)
- настроить трейсинг (grafana tempo)
- настроить логгирование (logging grafana loki) 

- TODO: использовать traefik вместо nginx чтобы поддерживать масштабирование (через динамическое добавление сервисов)?
- развернуть в swarn
- Сделать отказоустойчивый кластер на двух серверах
- Security and auth
- Middleware and plugins
- Нужен скрипт или контейнер инициализации (БД настроить и тп. чтобы не увеличивать время запуска проверяя это всё и это делал только один сервис)
- Docker swarm или k8s?

[//]: # (- Надо вынести всё в env настройки)

# Arhitecture
- Onion
- Solid
- Microservice

### Tools

- pipx
- pyenv
- poetry

- fastapi
- pydantic
- starlette
- httpx

#### DB

- [SQLAlchemy](https://www.youtube.com/watch?v=hYuGRgVXGwU&list=PLeLN0qH0-mCXARD_K-USF2wHctxzEVp40&index=1&ab_channel=%D0%90%D1%80%D1%82%D1%91%D0%BC%D0%A8%D1%83%D0%BC%D0%B5%D0%B9%D0%BA%D0%BE)
- OR SQLModel? https://sqlmodel.tiangolo.com/

#### Cache
- aiocache or async-lru
- redis? https://redis.io/

- docker?

#### Почему не только для IDE, так как на cicd тоже это всё надо проверять, все должны быть встроены в ci

- precommit? # Зачем, чтобы лишний раз не гонять cicd
- [mypy types cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- ruff? or - flake8? - isort?
- conventional commits
    - https://www.conventionalcommits.org/en/about/
    - https://github.com/commitizen-tools/commitizen
    - https://github.com/jorisroovers/gitlint
    - https://github.com/python-semantic-release/python-semantic-release
    - https://github.com/jgoodman8/pyhist

- pytest
- coverage # Как проверять что не упал процент?


### Install

#### TODO: попробовать установить с нуля и описать установку

### Run locally

- Install mypy plugin for your IDE
- На windows pycharm не видит wsl, надо установить mypy на виндовс с соотвествующим python

```bash
cd ~/YOUR_PROJECT_FOLDER
# Разные варианты запуска
uvicorn payment_service.main:app --reload
fastapi dev --host 0.0.0.0 payment_service/main.py  # абстракция
gunicorn youtube-video:app -w 4 -k uvicorn.workers.UvicornWorker  # наиболее производительный способ для прода чтобы утилизировать весь процессор на сервере # вертикальное масштабирование
# Вариант под prod
python -m payment_service.main
python payment_service/main.py
```

### Docker local / dev
```bash
# STAGE=dev,test or prod
STAGE=prod && docker build --rm -t payment-service:$STAGE --target $STAGE ./ && docker image prune --force

STAGE=prod && docker run --rm -it --entrypoint bash payment-service:$STAGE  # run container and go in to
STAGE=prod && docker run --rm --name payment-service-$STAGE -p 8000:8000 payment-service:$STAGE  # Run in place, remove after, see logs in console
STAGE=prod && docker run -d --name payment-service-$STAGE -p 8000:8000 payment-service:$STAGE
```

### Docker compose local / dev
```bash
docker image prune --force && docker compose up --build  # Проще
docker compose build && docker image prune --force && docker compose up  # Полная
```


### Code Quality

#### Во время активной правки

```bash
ruff check --watch  payment_service/main.py
ruff rule F821  # F821 is a rule name
```

#### Перед коммитом

```bash
ruff check .  # Check code

ruff check --select I --fix  # Sort (fix) imports only
ruff format .  # Format code

pytest  # -v for more details
# Запускай coverage тоже
mypy payment_service/
```
#### Нагрузочное тестирование
```bash
wrk -t 2 -c 10 -d 10 http://nzxt-home-pc:8001/books3  # Напрямую
wrk -t 4 -c 10 -d 10 http://payments.nklv.top/books3  # С traefik
wrk -t4 -c100 -d10s http://localhost:8080/health  # С nginx
```

### Docs

- http://localhost:8000/docs
- http://127.0.0.1:8000/redoc
- https://github.com/squidfunk/mkdocs-material  TODO: Заморочиться и поднять сайт с документацией?

### Refs

#### Templates
- Хороший FullStack Template https://github.com/fastapi/full-stack-fastapi-template/tree/master?tab=readme-ov-file
- Очень много под prod ready https://github.com/s3rius/FastAPI-template
- https://github.com/zhanymkanov/fastapi_production_template
- https://github.com/jonra1993/fastapi-alembic-sqlmodel-async
- Пример микросервиса https://github.com/q00Dree/fastapi-based-microservices/tree/master/src/movie-services
- Пример с тенажер https://github.com/szymon6927/hexagonal-architecture-python
- Пример статьи с gateway и rabit https://snimkar1905.medium.com/building-microservices-with-fastapi-and-rabbitmq-part1-1104dbd4ad96


-[mypy Playground](https://mypy-play.net/?mypy=latest&python=3.11&gist=d0a3e2279a7a6147541570967634f0da)

- https://solvit.space/roadmaps/fastapi-interactive?utm_source=tg_bot_artemshumeikobot&utm_medium=organic&utm_campaign=roadmap_fastapi

- Слоиская архитектура https://www.youtube.com/watch?v=8Im74b55vFc&ab_channel=%D0%90%D1%80%D1%82%D1%91%D0%BC%D0%A8%D1%83%D0%BC%D0%B5%D0%B9%D0%BA%D0%BE


