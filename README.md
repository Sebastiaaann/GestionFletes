# GestionFletes

#   VENV
-- Primero Crear entorno VENV

python -m venv nombre_del_entorno

# En Windows PowerShell, si aparece error de ejecución de scripts:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

nombre_del_entorno\Scripts\Activate

# PIP Necesarios para que funcione

pip install django

pip install django-widget-tweaks

# PDF

pip install reportlab

# EXCEL

pip install openpyxl


# Hacer migraciones

python manage.py migrate
python manage.py makemigrations


