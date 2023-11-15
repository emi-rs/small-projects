# Virtual Env
pip install virtualenv
python -m venv env

## Before every env on windows activation: 
Set-ExecutionPolicy Unrestricted -Scope Process
env/Scripts/activate.ps1

deactivate


# env variables
BASE_PATH - path to split images folder \
OUTPUT_PATH - path to output images folder \
PAGES - how many pages in each folder \
SPLITS - how many splits each page has \
OFFSET - pixel offset to move images up vertically