# Makefile for PyTexas 2014 Talk - Cody Lee <codylee@wellaware.us>

all: titan

titan:
	fig up -d

deploy:
	gunicorn index:app

test:
	nosetests -vv

