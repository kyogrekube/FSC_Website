@echo on
py -3 -m venv .venv
call .venv/scripts/activate
py -m pip install --upgrade pip
py -m pip install Django==5.1.1
call code .
deactivate