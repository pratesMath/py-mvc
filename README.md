<h1 align="center">Python - MVC</h1>

**Description**: Learning MVC Architecture in Python.

- Flask
- Pydantic
- SQL Alchemy

## Getting started

Follow step by step below to execute this project correctly:

```SH
# create venv
python3 -m venv .venv
source .venv/bin/activate # always use this command to activate venv (per terminal session)

# install dependencies
pip3 install -r requirements.txt

# if install some lib without using requirements.txt file
# you can put theses libs accessing .venv folder
.venv/bin/pip3 freeze > requirements.txt

# generate pylint file
pylint --generate-rcfile > .pylintrc

# pre-commit
pre-commit install

# most used flask cli commands
flask run # run flask app
flask shell # create/open flask instance
```

<br>
<div align="center">
  <h2>Thanks 2 everyone!</h2>
  <p>Made w/ 💙 by <a href="https://github.com/pratesMath">pratesMath</a>.</p>
</div>
