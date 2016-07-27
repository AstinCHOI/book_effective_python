
# Transitive dependencities

# $ pip3 show flask
# >>>
# ...
# Location: /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages
# Requires: Werkzeug, Jinja2, itsdangerous
# ...


# After python 3.4, you can use..
# $ python3 -m venv


# Before python 3.4, you should..
# $ pip install virtualenv


# $ pyenv /tmp/myproject
# $ cd /tmp/myproject
# $ source bin/activate
# (myproject)$ pip3 list
# (myproject)$ pip3 freeze > requirements.txt
# (myproject)$ deactivate

# ...
# (otherproject)$ pip3 install -r /tmp/myproject/requirements.txt
# (otherproject)$ pip3 list


