# vana-banguat
RESTful API on Python to access Banguats' information about change rate between types of currency.

## Overview
- scraper.py es el archivo en donde estan definidos los metodos para la obtencion de datos desde https://www.banguat.gob.gt/cambio/
- api.py es el API que utiliza los datos de entrada para consultar los datos de tipo de cambio, recibiendo los argumentos de fecha (o fechas) y el tipo de moneda. Para esto utiliza las funciones definidas en scraper.py y dependiendo de los argumentos consulta una fecha especifica o un rango de fechas.

### Funciones en scraper.py
- single_date(date, currency) es la funcion que se encarga de realizar la consulta hacia banguat con los datos de fecha y tipo de moneda. Esta devuelve el tipo de cambio de dolares expresado en quetzalas y el de euro expresado en quetzales haciendo la conversion por medio del tipo de cambio de dolar.
- range_dates(start_date, end_date, currency) la cual devuelve el tipo de cambio en quetzales cuando currency='USD' y en dolares cuando currency='EURO'.  
- range_dates() devuelve la primera y ultima fecha con datos disponibles dentro del rango. 
- El argumento date se espera en formato yyyy-mm-dd.
- El argumento currency pertenece a ['USD', 'EURO'].

## Running files
### 1. Requirements
- pip install pandas
- pip install -U Flask
- pip install flask-restful

### 2. Run API
python api.py

### 3. Test API
- Single date:
http://localhost:5000/items?date=2021-02-19&currency=USD

- Range of dates:
http://localhost:5000/items?start_date=2021-02-14&end_date=2021-02-17&currency=USD

## With Docker Compose
1. docker-compose build
2. docker-compose up

### Test
- Single date:
http://localhost:80/items?date=2021-02-19&currency=USD

- Range of dates:
http://localhost:80/items?start_date=2021-02-14&end_date=2021-02-17&currency=USD

### Try on the internet
- Single date:
http://3.140.5.13:80/items?date=2021-02-19&currency=USD

- Range of dates:
http://3.140.5.13:80/items?start_date=2021-02-14&end_date=2021-02-17&currency=USD

### Comentarios
Existe la posibilidad de retornar errores, esto es debido a que hay datos que no siempre son publicados por benguat y al consultar las tablas en el sitio la estructura de la pagina ha cambiado.
