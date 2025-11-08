#!/bin/sh
#	Author: Ruben Camacho Alvarez
#	DGTIC,UNAM@SEGURIDAD INFORMATICA
#
#	Description:
#
#	This shell script creates and configures the virtual environment to 
#	run the network packet sniffer securely.
#
#	Usage:
#
#	sh setup.sh
#
#	or, if the file is executable:
#
#	./setup.sh
#

on_error() {

	if [ $? -ne 0 ]; then

		echo "$1"

		exit 1

	fi

}


echo "Starting sniffer setup"

if cat /etc/os-release | grep -Eiq "(Ubuntu)|(Debian)"; then

	dpkg -l python3-venv 2> /dev/null | grep -Eq '^ii'

	if [ $? -ne 0 ]; then

		echo "Package 'python3-venv' is not installed"

		echo -n "Would you like to install it? [y/N]: "

		read confirmation

		if echo $confirmation | grep -Eiq '^Y'; then

			echo "Installing package..."

			sudo apt install -y python3-venv

			on_error "Error while trying to install the package"

		else

			on_error "The package will not be installed"

		fi

	fi

fi

echo "Creating virtual environment..."

python3 -m venv .

on_error "Error creating the virtual environment."

echo "Virtual environment created successfully"

echo "Activating the virtual environment..."

source ./bin/activate

on_error "Failed to activate the virtual environment"

echo "Virtual environment activated successfully"

echo "Installing required dependencies..."

pip install -r requirements.txt

on_error "Failed to install project dependencies"

echo "Sniffer setup complete"

