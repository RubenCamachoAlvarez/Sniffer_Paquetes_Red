#!/bin/bash
#
#	Autor: Ruben Camacho Alvarez
#
#	DGTIC-UNAM@SEGURIDAD_INFORMATICA
#
#	Descripcion:
#
#		Este script de shell para sistemas UNIX tiene la finalidad de llevar a cabo la
#		creacion y configuracion de un entorno virtual para ejecutar el sniffer de red de
#		manera segura.
#
#	Modo de ejecucion:
#
#		bash setup.sh
#

INVOCACION=${BASH_SOURCE[0]}

RUTA_DIRECTORIO_PADRE_RAIZ="$(dirname -- $INVOCACION)"

if [ $RUTA_DIRECTORIO_PADRE_RAIZ == "." ]; then

	RUTA_DIRECTORIO_PADRE_RAIZ="$(dirname -- "$(pwd)")"

	NOMBRE_DIRECTORIO_RAIZ="$(basename -- "$(pwd)")"

else

	NOMBRE_DIRECTORIO_RAIZ="$(basename -- $RUTA_DIRECTORIO_PADRE_RAIZ)"

	RUTA_DIRECTORIO_PADRE_RAIZ="$(dirname -- $RUTA_DIRECTORIO_PADRE_RAIZ)"

fi

NOMBRE_ENTORNO_VIRTUAL="env$NOMBRE_DIRECTORIO_RAIZ"


echo -e "\n-----------------------------------------------------"

echo -e "\nConfigurando entorno virtual de la aplicacion CLI\n"

echo "-----------------------------------------------------"


echo -e "\n> Cambiando a directorio $RUTA_DIRECTORIO_PADRE_RAIZ \n"

cd -- $RUTA_DIRECTORIO_PADRE_RAIZ

echo -e "> Creando directorio $NOMBRE_ENTORNO_VIRTUAL \n"

mkdir -- $NOMBRE_ENTORNO_VIRTUAL

echo -e "> Moviendo directorio $NOMBRE_DIRECTORIO_RAIZ dentro del directorio $NOMBRE_ENTORNO_VIRTUAL \n"

mv -- $NOMBRE_DIRECTORIO_RAIZ $NOMBRE_ENTORNO_VIRTUAL

echo -e "> Cambiando a directorio $NOMBRE_ENTORNO_VIRTUAL \n"

cd -- $NOMBRE_ENTORNO_VIRTUAL

echo -e "> Creando entorno virtual \n"

python -m venv .

echo -e "> Entorno virtual creando satisfactoriamente \n"

echo "-----------------------------------------------------"

echo -e "\nEntorno virtual listo para ejecutar la aplicacion CLI\n"

echo "-----------------------------------------------------"

echo -e "> Iniciando entorno virtual... \n"

source ./bin/activate

echo -e "\n> Cambiando a directorio $NOMBRE_DIRECTORIO_RAIZ \n"

cd -- $NOMBRE_DIRECTORIO_RAIZ

echo -e "> Instalando dependencias (requirements.txt) ...\n"

pip install -r requirements.txt

echo -e "> setup.sh ejecutado correctamente\n"

echo -e "> Todo preparado para ejecutar la aplicacion CLI\n"

