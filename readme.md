### Prequisition
- python3

### Installation
- Create virtual environment. eg. venv
```python
python3 -m venv venv
```
- Activate your virtual environment
```python
. venv/bin/Activate
```
- Install requirements
```python
pip install -r requirements.txt
```
- Run migration
```python
python manage.py migrate
```

### Agent account
After run migration, you'll be able to login to admin page http://localhost:8008/quotations-admin with agent account:

```
username: agent
password: agent
``` 