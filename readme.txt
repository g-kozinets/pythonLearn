Task 1:
C:\Python310>python -m venv c:\env_pyhton\myenv
C:\Python310>py -m ensurepip --upgrade
C:\Python310>pip install torch Keras --user
C:\Python310>pip install torch==1.12.1
C:\env_pyhton\myenv> -m pip freeze > requirements.txt
C:\env_pyhton\myenv2>python -m pip install -r requirements.txt

Task 2:
1) PS D:\PyCharmProjects> pip install pandas --user
2) Проект создан через PyCharm
3) через терминал ide деактивирую окружение, чтобы получить проект без окружения
(venv) PS D:\PyCharmProjects> deactivate

4) 
PS D:\PyCharmProjects> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
>>> 

5) PS D:\PyCharmProjects> .\venv\Scripts\activate   
6) 
(venv) PS D:\PyCharmProjects> python
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
>>>

