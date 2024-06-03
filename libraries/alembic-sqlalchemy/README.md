# alembic-sqlalchemy
A simple demonstrator of libraries usage.


## Run

```
alembic init alembic

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head

alembic revision --autogenerate -m "Add email column to User"

alembic upgrade head


```

Project structure after migrations:

```myapp/
    alembic/
        versions/
            <timestamp>_initial_migration.py
            <timestamp>_add_email_column_to_user.py
        env.py
        script.py.mako
    models.py
    main.py
    alembic.ini```