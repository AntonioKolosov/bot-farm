# Bot Farm


## Project structure
``` bash
├── .github
│   └── workflows
│       └── build.yaml
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── README.md
├── main.py
├── pytest.ini
├── requirements.txt
├── requirements_dev.txt
├── src
│   ├── __init__.py
│   ├── clients
│   │   └── tgclient
│   │       ├── __init__.py
│   │       ├── tgclientconfig.py
│   │       ├── tgclientmessage.py
│   │       ├── tgclientsetup.py
│   │       ├── tgclientutils.py
│   │       └── tgclientwebhook.py
│   ├── gtw
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── description.py
│   │   ├── internals
│   │   │   ├── __init__.py
│   │   │   └── tbotlogger.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   ├── inc_data_router.py
│   │   │   └── testrouter.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       └── tgindata.py
│   ├── handlers
│   │   ├── __init__.py
│   │   ├── handler.py
│   │   └── internal_handler.py
│   └── messanger
│       ├── __init__.py
│       ├── active_chats
│       │   ├── __init__.py
│       │   └── active_chats.py
│       ├── active_handlers
│       │   └── __init__.py
│       ├── internal_handler
│       │   └── __init__.py
│       ├── mess_dispatcher
│       │   ├── __init__.py
│       │   └── mess_dispatcher.py
│       └── schemas
│           ├── __ini__.py
│           └── processingdata.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── clients
    ├── gtw
    │   ├── test_app.py
    │   └── test_routers
    │       ├── __init__.py
    │       └── test_inc_data_router.py
    ├── handlers
    └── messanger
```

### Setup the project for the development
```bash
pip install -r requirements-dev.txt
```

### Run
```bash
uvicorn main:app --host 0.0.0.0 --port 8005
```

### Check from browser
1. http://127.0.0.1:8005/
```
Hello I am your Bot
```

2. http://127.0.0.1:8005/docs

Interactive Documentation

### Linting
```bash
flake8 -v src/
```

### Unit testing
```bash
pytest
```

### Git hooks
```bash
pre-commit run --all-files
```

### GitHub Actions
