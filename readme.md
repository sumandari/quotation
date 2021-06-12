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
  
### Demo  
  
![quot](https://user-images.githubusercontent.com/40058076/121774858-f5027f00-cbb6-11eb-8d5e-ff78c33fde5a.gif)
 
### Calculator

![image](https://user-images.githubusercontent.com/40058076/121778222-a5c54a00-cbc8-11eb-91a6-3a36d5efba88.png)
  
### PDF on web
![image](https://user-images.githubusercontent.com/40058076/121778259-c2fa1880-cbc8-11eb-81a3-563c44b1867b.png)
  
### Email on console

![image](https://user-images.githubusercontent.com/40058076/121774896-2ed38580-cbb7-11eb-8be7-d020a37068ed.png)
