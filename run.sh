#!/usr/bin/env bash
set -o errexit

gunicorn myproject.wsgi:application
