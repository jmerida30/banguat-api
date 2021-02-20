import pandas as pd
import datetime

# Funcion del Metodo 1, recibe la fecha y la moneda y devuelve el tipo de cambio en quetzales para esta.
def single_date(date, currency):

    # Extraemos los valores de dia, mes y anio para ser enviados a url de Banguat como argumentos.
    date_arr = date.split("-")
    year, month, day = date_arr[0], date_arr[1], date_arr[2]
    url = "https://www.banguat.gob.gt/cambio/historico.asp?ktipo=3&kdia=" + day + "&kmes=" + month + "&kanio=" + year + "&submit1=Consultar"

    # Se extraen las tablas generadas por la peticion para obtener los tipos de cambio.
    tables = pd.read_html(url)

    # La 3ra tabla en la pagina es la que contiene el valor de tipo de cambio para dolar.  
    dolar = tables[2]
    dolar = float(dolar.iloc[0, 1])

    # Se devuelve el tipo de cambio de dolares de ser este el tipo de cambio solicitado.
    if currency == "USD":
        return date, currency, dolar
    # Se devuelve el tipo de cambio de euros utilizando el valor de dolares que nos proporciona la tabla anterior. 
    elif currency == "EURO":
        euro = tables[3] # La 4ta tabla es la que contiene el valor de tipo de cambio para euros.
        euro = float(euro.iloc[11, 1])
        return [date, currency, euro * dolar]

# Funcion del Metodo 2, recibe rango de fechas y devuelve 
def range_dates(start_date, end_date, currency):

    # Extraccion de fecha de inicio.
    start_date_arr = start_date.split("-")
    start_year, start_month, start_day = start_date_arr[0], start_date_arr[1], start_date_arr[2]

    # Extraccion de fecha de fin.
    end_date_arr = end_date.split("-")
    end_year, end_month, end_day = end_date_arr[0], end_date_arr[1], end_date_arr[2]

    # Codificacion de moneda para url.
    moneda = ""
    if currency == "USD": moneda = "02"
    elif currency == "EURO": moneda = "24"
    
    # Extraccion de tabla de valores para tipo de cambio en la moneda solicitada.
    url = "https://www.banguat.gob.gt/cambio/historico.asp?kmoneda=" + moneda
    url += "&ktipo=5&kdia=" + start_day + "&kmes=" + start_month + "&kanio=" + start_year
    url += "&kdia1=" + end_day + "&kmes1=" + end_month + "&kanio1=" + end_year + "&submit1=Consultar"
    tables = pd.read_html(url)
    table = tables[2].iloc[:-1, 0:2]

    # Se adquieren las fechas de inicio y fin (cuyos datos se encuentran dentro de la tabla).
    start = datetime.datetime.strptime(table.iloc[0, 0], "%d/%m/%Y").strftime("%Y-%m-%d") 
    end = datetime.datetime.strptime(table.iloc[-1, 0], "%d/%m/%Y").strftime("%Y-%m-%d")
    
    # Se calcula el minimo, maximo y promedio de los tipos de cambio disponibles denro de la tabla.
    # Para el caso de tipo de moneda EURO este resultado es devuelto en dolares.
    min_rate = min(pd.to_numeric(table.iloc[:, 1])) 
    max_rate = max(pd.to_numeric(table.iloc[:, 1]))
    mean = pd.to_numeric(table.iloc[:, 1]).mean()

    # Devolucion de los datos
    return [start, end, currency, mean, max_rate, min_rate]
