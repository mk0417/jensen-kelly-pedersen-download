# Download Jensen, Kelly and Pedersen (JKP) data

A simple Python package for downloading JKP data.

## Installation

I will not release a PyPI package. Therefore, you can install `jkp_download` directly from the GitHub repository using `pip`:

```bash
pip install git+https://github.com/mk0417/jensen-kelly-pedersen-download.git
```

## Usage

```python
import jkp_download as jkp
```

To view all available markets, regions, factors, themes, weighting shcemes and frequencies:

```python
avail_market = jkp.list_markets()
avail_region = jkp.list_regions()
avail_factor = jkp.list_factors()
avail_theme = jkp.list_themes()
avail_weight = jkp.list_weights()
avail_freq = jkp.list_freq()
```

To download details of factors and markets:

```python
doc_dl('factor')

doc_dl('market')
```

Use `factor_dl` to download long-minus-short returns, and use `port_dl` to download all tercile portfolio returns.

```python
# Download monthly long-short returns of all 153 US factors
data = jkp.factor_dl('usa', 'all_factors', 'monthly', 'ew')

# Download daily long-short return of value theme for all available markets
data = jkp.factor_dl('all_countries', 'value', 'daily', 'vw')

# Download monthly tercile portfolio returns (capped value-weighted) of single factor, asset-to-book equity, in UK
data = jkp.port_dl('gbr', , 'at_be', 'monthly', 'vw_cap')
```

Note: Themes are not allowed for `port_dl`.

## Data source

https://jkpfactors.com/data

