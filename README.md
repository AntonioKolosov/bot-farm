# Bot Farm
This is an implementation of backend infrastructure.  
My bot farm lets to manage a lot of different bot types with different messengers(Telegram, Whatsapp, etc.)  
In the current version available only to Telegram client. 
## Project structure
``` bash
├── README.md
├── .gitignore
├── .github
│   ├── workflows
│       ├── build.yaml
├── .pre-commit-config.yaml
├── data
├── datatopics
│   ├── fake.json
│   └── test.json
├── main.py
├── pytest.ini
├── requirements.txt
├── requirements_dev.txt
├── src
│   ├── gtw
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── description.py
│   │   ├── internals
│   │   │   ├── __init__.py
│   │   │   ├── tbotlogger.py
│   │   │   └── utilites.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   └── inc_data_router.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       └── tgindata.py
│   ├── handlers
│   │   ├── __init__.py
│   │   ├── active_handlers.py
│   │   ├── handler.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   └── topic.py
│   │   ├── simple_handler.py
│   │   └── topics_loader.py
│   ├── mess_broker
│   │   ├── __init__.py
│   │   ├── active_chats
│   │   │   ├── __init__.py
│   │   │   └── active_chats.py
│   │   ├── mess_dispatcher
│   │   │   ├── __init__.py
│   │   │   └── mess_dispatcher.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       └── processingdata.py
│   └── services
│       ├── __init__.py
│       ├── requests.py
│       ├── service.py
│       ├── services_list.py
│       └── tgservice
│           ├── __init__.py
│           ├── tgapi.py
│           └── tgservice.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── gtw
│   │   ├── __init__.py
│   │   ├── test_app.py
│   │   └── test_routers
│   │       ├── __init__.py
│   │       └── test_inc_data_router.py
│   ├── handlers
│   │   └── __init__.py
│   ├── mess_broker
│   │   └── __init__.py
│   └── services
│       ├── __init__.py
│       └── test_tgclientmessage.py
```

### Setup the project for the development
For this project will be installed:
* [fastapi](https://fastapi.tiangolo.com/) - popular framework for API's
* [flake8](https://flake8.pycqa.org/en/latest/) - for linting
* [httpx](https://www.python-httpx.org/) -  HTTP client for Python 3
* [pip](https://pypi.org/project/pip/) - for install packages
* [pipdeptree](https://pypi.org/project/pipdeptree/) - for sorting packages
* [pre-commit](https://pre-commit.com/) - Git hook scripts are useful for identifying simple issues before submission to code review.
* [pyngrok](https://pypi.org/project/pyngrok/) - a reverse proxy tool that opens secure tunnels from public URLs to localhost
* [pytest](https://docs.pytest.org/en/7.3.x/) - for unit tests
* [python-dotenv](https://pypi.org/project/python-dotenv/) - for reading .env files
* [uvicorn](https://www.uvicorn.org/) - an ASGI web server implementation for Python.
```bash
pip install -r requirements-dev.txt
```

### Run
```bash
uvicorn main:app --host 0.0.0.0 --port 8005 (or your_port)
```

### Check from browser
1. http://127.0.0.1:8005/
```
Hello I am your Bot
```

2. http://127.0.0.1:8005/docs

Interactive Documentation and tests via OpenAPI

### Linting
```bash
flake8 -v --max-line-length=79 --max-doc-length=72 --ignore=E203,W503 ./src
```

### Unit testing
```bash
pytest
```
