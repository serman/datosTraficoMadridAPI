# datosTraficoMadridAPI
# create virtual env
python3 -m venv datosTraficoApi

source venv/bin/activate
# create virtual env
git clone git@github.com:serman/datosTraficoMadridAPI.git
cd datosTraficoMadridAPI

#descargamos submodulo https://github.com/serman/VisorDatosTraficoMadrid
git submodule update --init --recursive
cd visortrafico_backend/consultas/VisorDatosTraficoMadrid
git pull https://github.com/serman/VisorDatosTraficoMadrid.git master

#desde el directorio raiz de instalacion ejecutamos el servidor django.
python manage.py runserver 0.0.0.0:80080

