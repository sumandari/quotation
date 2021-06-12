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
- Run development server
```python
python manage.py runserver 8008
```

### Agent account
After run migration, you'll be able to login to admin page http://localhost:8008/quotations-admin with agent account:

```
username: agent
password: agent
``` 

### Add On price
You can change the add price on http://localhost:8008/quotations-admin/quotations/addonprice/

### Send PDF and render on web
There's another function to send email other than api, you can send your request with url : http://localhost:8008/quotation/send_email/<id>/

### Email
We are using `django.core.mail.backends.console.EmailBackend` to send the email. We don't setup prod email here.

### Notes
This is not a production ready code.
