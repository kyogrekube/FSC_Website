@echo off

set venvpath=.venv
set django__ver=5.1.1

echo Setting up FSC Website project (Django %django__ver%)...
echo -^>creating virtual environment: %venvpath%/
py -3 -m venv %venvpath%
echo -^>installing Django %django__ver% in %venvpath%/
call .venv/scripts/activate
py -m pip install --upgrade pip
py -m pip install Django==5.1.1
echo Done