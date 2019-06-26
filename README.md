# queryf

### Apache Configuration

```bash
$ sudo apt update
$ sudo apt install apache2
$ sudo systemct1 status apache2
$ sudo ufw allow 80/tcp
$ sudo ufw allow 443/tcp
$ sudo ufw reload
```

### Flask Installation

```bash
$ pip install flask
$ pip install SQLAlchemy
$ pip install flask_sqlalchemy
$ pip install flask_script
```

### Web Runserver

```bash
$ git clone https://github.west.isilon.com/rcheng/bugzilla-query.git
$ cd bugzilla-query
$ export FLASK_APP=runserver.py
$ flask run --host 0.0.0.0
```




