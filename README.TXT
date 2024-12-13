Pasos para visualizar la pagina
1. Crear entorno virtual, en la terminal ejecutar el siguiente comando
python -m venv myvenv
2. Activar entorno virtual
./myvenv/Scripts/activate
3.Instalar requerimientos (django-user-agents)
pip -m pip install --upgrade pip
pip install -r requirements.txt

4. visualizar la pagina
py manage.py runserver

Nota importante: cuando cambie a modo celular, actualizar la pagina para que se actualize la vista
y poder ver el boton de descarga.