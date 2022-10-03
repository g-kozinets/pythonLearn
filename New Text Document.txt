C:\Python310>python -m venv c:\env_pyhton\myenv
C:\Python310>py -m ensurepip --upgrade
C:\Python310>pip install torch Keras --user
C:\Python310>pip install torch==1.12.1
C:\env_pyhton\myenv> -m pip freeze > requirements.txt
C:\env_pyhton\myenv2>python -m pip install -r requirements.txt