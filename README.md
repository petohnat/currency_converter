# Currency converter

## Synopsis

Simple currency converter package. Program supports 109 various currency
shortcuts and symbols. Program is using http://rate-exchange-1.appspot.com API
for online conversion and retrieves data in json format.
For various currency symbols program uses dictionary, which was retrieved from http://www.xe.com/symbols.php.

## Parameters
- --amount - amount which we want to convert - float
- --input_currency - input currency - 3 letters name or currency symbol
- --output_currency - requested/output currency - 3 letters name or currency symbol

## Functionality
- if output_currency param is missing, convert to all known currencies
- if more currencies are using the same currency symbol, program chooses
    default currency name for conversion.
    (default currency names are specified in currenciesDictionary.py)

## Installation and Requirements

Requirements:
- Python 2.7
- simplejson package
- beautifulsoup4 package
- Internet Connection

For correct functioning, you need to have installed all packages.

## Examples
- json with following structure.
```
{
    "input": {
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```

```
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": "2676.59"
    }
}
```
```
./currency_converter.py --amount 0.9 --input_currency ¥ --output_currency AUD
{
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": "0.1763172"
    }
}
```
```
./currency_converter.py --amount 10.92 --input_currency £
{
    "input": {
        "amount": 100.0,
        "currency": "GBP"
    },
    "output": {
        "AFN": "8713.35",
        "ALL": "15890.1",
        "ANG": "230.121",
        "ARS": "1968.9",
        "AUD": "174.06",
        "AWG": "230.665",
        "AZN": "217.333",
        "BAM": "230.673",
        .
        .
        .
    }
}
```

## Author
Peter Hnat (peto.hnat13@gmail.com)

