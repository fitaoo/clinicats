@echo off
cd /d C:\Users\Me\Documents\clinicats\clinicats
call venv\Scripts\activate.bat
python manage.py runserver 0.0.0.0:8000
pause
