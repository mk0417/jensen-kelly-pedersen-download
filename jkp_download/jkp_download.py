import polars as pl
from polars import col as c
import pandas as pd


data_url = 'https://jkpfactors-data.s3.amazonaws.com/public'
doc_url = 'https://github.com/bkelly-lab/jkp-data/raw/main/src/jkp/data/resources'

def doc_dl(doc):
    if doc == 'market':
        df = pl.read_excel(f'{doc_url}/country_classification.xlsx')
    if doc == 'factor':
        df = pl.read_excel(f'{doc_url}/factor_details.xlsx')

    return df

def list_markets():
    df = doc_dl('market')
    market_list = df.get_column('excntry').str.to_lowercase().to_list()
    return ['all_countries'] + sorted(market_list)

def list_regions():
    return ['world', 'world_ex_us', 'all_regions', 'developed', 'emerging', 'frontier']

def list_factors():
    df = doc_dl('factor')
    factor_list = df.filter(c.abr_jkp.is_not_null()).get_column('abr_jkp').to_list()
    return ['all_factors'] + sorted(factor_list)

def list_themes():
    return [
        'mkt', 'all_themes', 'accruals', 'debt_issuance', 'investment',
        'low_leverage', 'low_risk', 'momentum', 'profit_growth', 'profitability',
        'quality', 'seasonablity', 'size', 'short_term_reversal', 'value']

def list_weights():
    return ['ew', 'vw', 'vw_cap']

def list_freq():
    return ['monthly', 'daily']

def _read_data(url):
    return pd.read_csv(url, engine='pyarrow').pipe(lambda x: pl.from_pandas(x))

def factor_dl(market, factor, freq, weight):
    url = f'{data_url}/%5B{market}%5D_%5B{factor}%5D_%5B{freq}%5D_%5B{weight}%5D.zip'
    return _read_data(url).sort('location', 'name', 'date')

def port_dl(market, factor, freq, weight):
    url = f'{data_url}/portfolios/%5B{market}%5D_%5B{factor}%5D_%5B{freq}%5D_%5B{weight}%5D.zip'
    return _read_data(url).with_columns(c.pf.cast(pl.Int8)).sort('location', 'name', 'pf', 'date')

