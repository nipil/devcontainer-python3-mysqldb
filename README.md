# test python3-mysqldb

Open in dev container, and verify that database can be used :

    echo 'SELECT NOW();' | mariadb --host=${MARIADB_HOST} --user=${MARIADB_USER} --database=${MARIADB_DATABASE} --password=${MARIADB_PASSWORD}

Test library usage :

    ./test.py

Optionnaly, check database content :

    echo 'SELECT * FROM tete;' | mariadb --host=${MARIADB_HOST} --user=${MARIADB_USER} --database=${MARIADB_DATABASE} --password=${MARIADB_PASSWORD}

Documentation of the library : https://mysqlclient.readthedocs.io/
