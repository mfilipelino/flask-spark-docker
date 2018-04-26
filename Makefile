apt-get-install:
	sudo apt-get install -y virtualenv python-pip

venv:
	virtualenv -p python3 envname

requirements:
	venv/bin/python3 venv/bin/pip3 install -r requirements.txt

python-install: 
	venv requirements

install: 
	node-install python-install

build:
	venv/bin/python3 manage.py runserver

test:
	venv/bin/python3 manage.py test

run-server:
	venv/bin/python3 manage.py runserver

python-version:
	venv/bin/python3 --version

clean:
	rm -rf venv
	