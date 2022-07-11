VENV = venv
VBIN = $(VENV)/bin
PKG = bday_reminder

NMBIN = node_modules/.bin

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

$(NMBIN)/sass:
	yarn install

$(PKG)/static/css/style.css: $(NMBIN)/sass
	$(NMBIN)/sass --style compressed $(PKG)/static/scss/style.scss:$(PKG)/static/css/style.css

start: $(VBIN)/python $(PKG)/static/css/style.css
	$(VBIN)/pip install -e .
	$(VBIN)/python $(PKG)

user: $(VBIN)/python
	$(VBIN)/python scripts/dummy.py

.PHONY: all clean start user