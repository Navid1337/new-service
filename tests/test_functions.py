# Test mot kod.

import pytest
from application.func import slicing_iso_8601, api_url_to_pandas_dataframe
import pandas as pd


def test_slicing_iso_8601():                                            # Testar att gamla tabellen tas bort och nya finns med i pandas DataFrame.
    url = f"https://www.elprisetjustnu.se/api/v1/prices/2023/01-01_SE1.json"
    df = api_url_to_pandas_dataframe(url)                               # Anropar funktion för att skapa en pandas-tabell.
    
    df_result = slicing_iso_8601(df, 'time_start', 'new_time_start')    # Anropar funktionen för att slica iso-8601

    assert 'new_time_start' in df_result.columns                        # Test för att se om den nya kolumnen finns
    assert 'time_start' not in df_result.columns                        # Test för att se att den gamla kolumnen INTE finns.


def test_api_url_to_pandas_dataframe():                                 # Testar om en DataFrame returneras från en API-endpoint.
    url_1 = f"https://www.elprisetjustnu.se/api/v1/prices/2022/10-25_SE1.json"
    df_result = api_url_to_pandas_dataframe(url_1)                      # Anropar funktionen för att skapa DataFrame från URL:en.

    assert isinstance(df_result, pd.DataFrame)                          # Kontrollera om det returnerade värdet är en DataFrame.
                                                                        # https://www.w3schools.com/python/ref_func_isinstance.asp

