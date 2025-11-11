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
#	. setup.sh
#
#	or, if using bash
#
#	source setup.sh
#

echo "Starting sniffer setup"

if cat /etc/os-release | grep -Eiq "(Ubuntu)|(Debian)"; then

	dpkg -l python3-venv 2> /dev/null | grep -Eq '^ii'

	if [ $? -ne 0 ]; then

		echo "Package 'python3-venv' is not installed"

		echo -n "Would you like to install it? [y/N]: "

		read confirmation

		if echo $confirmation | grep -Eiq '^Y'; then

			echo "Installing package..."

			if ! sudo apt install -y python3-venv; then

				echo "Error while trying to install the package" >&2

				return 1

			fi

		else

			echo "The package will not be installed" >&2

			return 1

		fi

	fi

fi

echo "Creating virtual environment..."

if ! python3 -m venv .; then

	echo "Error creating the virtual environment." >&2

	return 1

fi

echo "Virtual environment created successfully"

echo "Activating the virtual environment..."

if ! . bin/activate; then

	echo "Failed to activate the virtual environment" >&2

	return 1

fi

echo "Virtual environment activated successfully"

echo "Installing required dependencies..."

if ! pip install -r requirements.txt; then

	echo "Failed to install project dependencies" >&2

	return 1

fi

echo "Sniffer setup complete"

