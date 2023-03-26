# Development Environments

* sqlalchemy
* alembic
* asyncpg
* dotenv

# Purposes
1. support asyncio based on fastapi

2. only one root module



# How to do that

## 1. pyenv

```bash
pyenv local 3.9.16
```

## 2. pdm

### 2.1. configure virtual environment

```bash
pdm config --local venv.in_project True
pdm config --local venv.backend venv
```

or

```bash
./01_setup_pdm_toml.sh
```

### 2.2. edit pyproject.toml

* project.name
* project.version
* project.authors


### 2.3. using PySide6 and cx_freeze together (optional)

```toml
[build-system]
requires = ["pdm-backend"]
build-backend = "pdm.backend"
```

## 3. alembic

### 3.1. folders

`migrations > versions` is required


### 3.2. configurations

change belows for using `.env`

1. $PROJECT_ROOT/alembic.ini

2. $PROJECT_ROOT/migrations/script.py.mako

3. $PROJECT_ROOT/migrations/env.py


### 3.3. include_object aded

The below function should added into `$PROJECT_ROOT/migrations/env.py`.

```python
def include_object(object, name, type_, reflected, compare_to):
    if type_ == 'table' and object.info.get("skip_autogenerate", False):
        return False
    elif type_ == "column" and object.info.get("skip_autogenerate", False):
        return False
    return True
```


## 4. update `.env` file

1) edit .env for setting database up

```bash
DB_USER=<DB_USER>
DB_PASS=<DB_PASSWORD>
DB_HOST=<DB_HOST>
DB_PORT=<DB_PORT>
DB_NAME=<DB_NAME>

DB_ECHO=true
DB_POOL_PRE_RING=true

LOG_LEVEL = debug
```


## 5. sqlalchemy

### 5.1. using sqlmodel together
as of March 26 2023, sqlmodel is 0.0.8

To support the above sqlmodel, currently `1.4.41` version of sqlalchemy is required. (Not supported 2.x)

```bash
pdm add sqlalchemy==1.4.41
```

### 5.2. async db session

using fastapi_async_sqlalchemy with 0.3.14 version

```python
from fastapi_async_sqlalchemy import db

async db.session.execute(....)
```


```bash
pdm add git+https://github.com/h0rn3t/fastapi-async-sqlalchemy.git
```

## 6. pdm install

```bash
pdm install
```

## 7. git (optional)

```bash
git init
```


# References

## pdm install

https://pdm.fming.dev/latest/usage/venv/#virtualenv-auto-creation

> When you run pdm install the first time on a new PDM-managed project, whose Python interpreter is not decided yet, PDM will create a virtualenv in <project_root>/.venv, and install dependencies into it.

## pdm config

https://pdm.fming.dev/latest/usage/project/#configure-the-project


> By default, the configuration are changed globally, if you want to make the config seen by this project only, add a --local flag:

```bash
pdm config
```

```bash
pdm config --local pypi.url "https://test.pypi.org/simple"
```

