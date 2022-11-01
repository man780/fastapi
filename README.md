# Tutorial

```cmd
pip install -r requirements.txt
```

### Docker alembic run migration
```cmd
docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head
```

```cmd
docker-compose build
docker-compose up
```
