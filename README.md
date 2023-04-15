# Bot Farm


## Project structure
``` bash
├── .github
│   └── workflows
│       └── build.yaml
├── app
│   ├── __init__.py
│   ├── app.py
│   ├── description.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── hook.py
│   └── schemas
│       ├── __init__.py
│       └── tbdata.py
├── tests
│   ├── __init__.py
│   └── test_app.py
├── .gitignore
├── .pre-commit-config.yaml
├── main.py
├── Dockerfile
├── README.md
├── requirements.txt
└── requirements_dev.txt
```

### Setup the project for the development
```bash
pip install -r requirements-dev.txt
```

### Run
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Check from browser
1. http://127.0.0.1:8000/
```
Hello I am your Bot
```

2. http://127.0.0.1:8000/docs

Interactive Documentation

### Linting
```bash
flake8 -v app/
```

### Unit testing
```bash
pytest tests/test_app.py
```

### Git hooks
```bash
pre-commit run --all-files
```

### GitHub Actions
