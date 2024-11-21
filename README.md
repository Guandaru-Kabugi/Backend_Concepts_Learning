# Backend_Concepts_Learning


# Migration
from sqlite to mysql database

while on sql, use the following command
python3 manage.py dumpdata --exclude=contenttypes >datadump.json

while on mysql, run the following command
python3 manage.py loaddata datadump.json