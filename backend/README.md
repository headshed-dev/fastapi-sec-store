# Setup

as this backend project uses Python, ideally, use a virtural environment setup :

```bash
virtualenv env
source env/bin/activate
```

install python dependencies with 

```bash
pip install -r requirements.txt
```

create and setup db with 

```bash
alembic upgrade head
```

run the app with 

```bash
uvicorn main:app --reload
```

or without docs with 

```bash
DISABLE_DOCS=true uvicorn main:app 
```