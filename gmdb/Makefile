# Makefile for PyTexas 2014 Talk - Cody Lee <codylee@wellaware.us>

all: test deploy

deploy:
	gunicorn -k eventlet -w 25 --reload -b 0.0.0.0:8080 index:app

test:
	nosetests -vv

