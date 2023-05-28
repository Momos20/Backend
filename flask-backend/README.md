# Starting this App

```bash
docker-compose up -d
# Populate the DB

docker-compose run --rm -v ${PWD}:/opt/src -w /opt/src mysql bash

mysql -ucompanies -hmysql -p  # write exit
mysql -ucompanies -hmysql -p companies < ./db/creation.sql
```
