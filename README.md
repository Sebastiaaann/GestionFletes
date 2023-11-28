# GestionFletes


-- Primero Crear entorno VENV
#   VENV
python -m venv nombre_del_entorno

nombre_del_entorno\Scripts\Activate

listo

-- Instalar Requirements
#   requirements

pip install -r requirements.txt

-- Migraciones
# Hacer migraciones

python manage.py migrate
python manage.py makemigrations


