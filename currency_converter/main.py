import argparse
import sys
from currenciesConverter import CurrenciesConvertor
from currenciesDictionary import CurrenciesDictionary


# Program Main
if __name__ == "__main__":

    # Parse arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-a", "--amount", type=float, required=True,
                           help="Amount which we want to convert - float")
    argParser.add_argument("-i", "--input_currency", type=str, required=True,
                           help="Input currency - 3 letters name or currency symbol")
    argParser.add_argument("-o", "--output_currency", type=str, required=False,
                           help="Requested/output currency - 3 letters name or currency symbol")
    args = argParser.parse_args()

    # Check letters or symbol of input currency
    if len(args.input_currency) > 3:
        print("Input currency - 3 letters name or currency symbol")
        sys.exit(-1)

    # Check letters or symbol of output currency
    if args.output_currency is not None:
        if len(args.output_currency) > 3:
            print("Output currency - 3 letters name or currency symbol")
            sys.exit(-1)

    # Init dictionary with currency symbols and names
    dictionary = CurrenciesDictionary()

    # Get all currencies of given input symbol
    convertFromCurrencies = dictionary.getCurrencyCode(args.input_currency)

    # If not output specified
    if(args.output_currency == None):
        convertToCurrencies = dictionary.getAllCurrencies()
    else:
        convertToCurrencies = dictionary.getCurrencyCode(args.output_currency)

    convertor = CurrenciesConvertor(args.amount, convertFromCurrencies, convertToCurrencies)
    convertor.startConversion()

    # Print result of conversion
    convertor.getConversionResult()
