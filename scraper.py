import pandas as pd

def single_date(date, currency):
    date_arr = date.split("-")
    year, month, day = date_arr[0], date_arr[1], date_arr[2]
    url = "https://www.banguat.gob.gt/cambio/historico.asp?ktipo=3&kdia=" + day + "&kmes=" + month + "&kanio=" + year + "&submit1=Consultar"
    tables = pd.read_html(url)

    dolar = tables[2]
    dolar = float(dolar.iloc[0, 1])

    if currency == "USD":
        return date, currency, dolar
    elif currency == "EURO":
        euro = tables[3]
        euro = float(euro.iloc[11, 1])
        return date, currency, euro * dolar
