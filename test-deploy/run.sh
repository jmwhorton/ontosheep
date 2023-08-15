#!/bin/sh

# Wait for the database to be ready
sleep 20

python setup_repo.py

python ews_calculator.py

