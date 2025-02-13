import pandas as pd
import requests
import json



def slicing_iso_8601(DataFrame, old_column_name, new_column_name):
    """Tar en pandas-column, slicar iso-8601 till hh:mm, skapar en ny column och tar bort den gamla.
    Args:
        DataFrame: Pandas DataFrame
        old_column_name (_type_): Namnet på kolumnen man vill slica
        new_column_name (_type_): Vad för namn man vill ha på den nya kolumnen.
    Returns:
        _type_: _Returnerar en modifierad Pandas-tabell_"""
    DataFrame[new_column_name] = DataFrame[old_column_name].str[11:16]  # Slicar bort allt förutom hh:mm.
    del DataFrame[old_column_name]                                      # Tar bort gamla kolumnen.
    return DataFrame                                                    # Returnerar nya DataFrame.


def api_url_to_pandas_dataframe(url):
    """Tar en API-endpoint och konverterar den till en pandas DataFrame.
    Args:
        url (str): URL till API-endpoint.
    Returns:
        pd.DataFrame: En DataFrame med data från API-endpoint"""
    response = requests.get(url)                    # Hämtar data från URL:en.
    response_string = response.text                 # Konverterar svaret till en sträng.
    response_list = json.loads(response_string)     # Omvandlar strängen till en Python-lista.
    df = pd.DataFrame(response_list)                # Skapar en pandas DataFrame av listan.
    return df                                       # Returnerar den skapade DataFramen.
