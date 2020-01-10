## Run locally

Install the required dependencies
```
$ pip install -r requirements.txt
```

Then create a new PostgreSQL database
```postgresql
create database aceee;
```

You can use any database name you want, but do not forget to change it in the settings

```python
# crawler/settings.py
DATABASE = {
    'drivername': 'postgres',
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': '5432',
    'username': os.getenv('POSTGRES_USER', 'postgres'),
    'password': os.getenv('POSTGRES_PASSWORD', 'pass'),
    'database': os.getenv('POSTGRES_DB', 'aceee')
}
```

Run spider with 
```
scrapy crawl aceee
```

## Run with docker-compose

In the project directory run
```
docker-compose build
```

followed by
```
docker-compose up
```

This will start the PostgreSQL service and initiate crawling the spider. 

