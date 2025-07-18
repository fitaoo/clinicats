@echo off
REM Activar el entorno virtual (ajusta la ruta si usas uno)
cd C:\Users\Fitaot\Documents\Python\clinicats

REM Si tienes un entorno virtual llamado 'venv' dentro de la carpeta del proyecto:
call venv\Scripts\activate.bat

REM Iniciar el servidor Django
python manage.py runserver 0.0.0.0:8000

REM Pausar para mantener la ventana abierta si hay errores
pause
