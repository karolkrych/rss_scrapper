## Description
This application contains API for exchange rates and scrappers for retrieving data about exchange rates.

## Installation

For development: all you need to do is to have docker installed and repo locally, then type this line in directory with 
`docker-compose.yml` file:

```
docker-compose up
```

## Usage

#### Getting exchange rates 
Type this command to get into docker container
```
docker-compose exec web bash
```
then, type this, to run scrapper and create exchange rates records in your local db
```
cd rss_scrapper
python manage.py run_currency_value_scrapper
```

#### Testing API 
You can check and test API with Swagger - it's on main local address - 127.0.0.1:8000

`/currencies/currencies_values/` URL contains filter `currency`, it can be used like this:

```
http://127.0.0.1:8000/currencies/currencies_values/?currency=10
```

where "10" is currency id.