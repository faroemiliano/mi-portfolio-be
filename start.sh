#!/usr/bin/env bash
python manage.py migrate --noinput
gunicorn mi_portfolio_be.wsgi:application
