# Django API + VueJS + Apollo + Postgraphile

This project is forked from here; read that README first.

## Database Setup

Assuming Docker Machine:

*TODO update these to superuser credentials for --watch*
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

## Test Data

```python
from api.models import TodoItem

items = [
    TodoItem(text='Use GraphQL'),
    TodoItem(text='?'),
    TodoItem(text='Profit')
]
TodoItem.objects.bulk_create(reversed(items))
```

## Postgraphile

To install and run (use the `--watch` flag to auto-update
on schema changes; this requires superuser privileges!):

```bash
$ npm install -g postgraphile
$ postgraphile -c "postgres://<user>:<pass>@<host>/testdb" --watch
```

Try the following to see if everything's working:

```graphql
{
  allApiTodoitems(orderBy: PRIMARY_KEY_DESC) {
    nodes {
      id
      text
    }
  }
}
```

and you should get:

```json
{
  "data": {
    "allApiTodoitems": {
      "nodes": [
        {
          "id": 3,
          "text": "Use GraphQL"
        },
        {
          "id": 2,
          "text": "?"
        },
        {
          "id": 1,
          "text": "Profit"
        }
      ]
    }
  }
}
```

