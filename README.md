# datosTraficoMadridAPI
Hace falta tener instalado python3 virtualenv y pip
## create virtual env
python3 -m venv datosTraficoApi

source venv/bin/activate

## get code
git clone git@github.com:serman/datosTraficoMadridAPI.git
cd datosTraficoMadridAPI

## descargamos submodulo 

desde https://github.com/serman/VisorDatosTraficoMadrid
git submodule update --init --recursive
cd visortrafico_backend/consultas/VisorDatosTraficoMadrid
git pull https://github.com/serman/VisorDatosTraficoMadrid.git master


Desde el directorio raiz de instalacion instalamos dependencias:
pip install -r requeriments.text
 
#ejecutamos el servidor django.
python manage.py runserver 0.0.0.0:80080

