#!/usr/bin/env bash
set -o errexit

cd apartment_management

python manage.py collectstatic --no-input
python manage.py migrate
