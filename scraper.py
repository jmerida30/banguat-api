import pandas as pd

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
        euro = tables[3]
        euro = float(euro.iloc[11, 1])
        return date, currency, euro * dolar
