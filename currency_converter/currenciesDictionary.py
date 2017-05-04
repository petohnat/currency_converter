from parseTableToJSON import parseTable


class CurrenciesDictionary:
    # Init currencies dictionary
    def __init__(self):
        self.currencies = parseTable()
        # Default values of duplicates currencies symbols
        self.duplicates = {'36': 'USD', '163': 'GBP', '165': 'CNY', '8361': 'KRW', '8364': 'EUR', '402': 'AWG'}

    # Get currencies names of given currency symbol
    def getCurrencyCode(self, currSymbol):

        convertingToCurrenciesNames = []

        for currency, uniCode in self.currencies.items():

            # Check duplicates symbols
            try:
                utf8Symbol = str(ord(currSymbol.decode('utf-8')))
                if utf8Symbol in self.duplicates:
                    convertingToCurrenciesNames.append(self.duplicates[str(ord(currSymbol.decode('utf-8')))])
                    # singleCurrencyName = self.duplicates[str(ord(currSymbol.decode('utf-8')))]
                    return convertingToCurrenciesNames

            except:
                # Compare symbol or name of currency
                if currSymbol.decode('utf-8') == uniCode or currSymbol.decode('utf-8') == currency:
                    convertingToCurrenciesNames.append(currency)

        return convertingToCurrenciesNames

    def getAllCurrencies(self):
        convertingToCurrenciesNames = []
        for currency, uniCode in self.currencies.items():
            convertingToCurrenciesNames.append(currency)

        return convertingToCurrenciesNames
