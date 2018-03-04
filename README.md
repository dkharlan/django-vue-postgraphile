# Django API + VueJS + Apollo + Postgraphile

This project is forked from here; read that README first.

## Database Setup

Assuming Docker Machine:

```bash
$ brew install postgresql   # for the command line tools
$ docker run --name postgresql10-test       \
      -e POSTGRES_USER=<admin user>     \
      -e POSTGRES_PASSWORD=<admin password> \
      -p 5432:5432                          \
      -d                                    \
      postgres:10-alpine
$ createdb -h <docker machine ip> -U <admin user> testdb
$ createuser -h <docker machine ip> -U <admin user> testuser
$ psql -h <docker machine ip> -U <admin user>
testdb=# \password testuser
testdb=# \q
```

Then modify `config/db.local.json` to match.
