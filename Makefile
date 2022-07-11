VENV = venv
VBIN = $(VENV)/bin
PKG = bday_reminder

all: start

clean:
	rm -rf venv
	rm -rf *.egg-info
	rm -rf __pycache__

	rm -rf $(PKG)/static/css
	rm -rf $(PKG)/bday.db

	rm -rf node_modules

$(VBIN)/python:
	python -m venv venv
	chmod +x venv/bin/activate
	./venv/bin/activate

node_modules:
	yarn install

$(PKG)/static/css/style.css: node_modules
	sass --style compressed $(PKG)/static/scss/style.scss:$(PKG)/static/css/style.css

start: $(VBIN)/python $(PKG)/static/css/style.css
	pip install -e .
	python $(PKG)


.PHONY: all clean start