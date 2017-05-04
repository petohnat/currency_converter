import urllib2
import json


class CurrenciesConvertor:
    # Init currencies dictionary
    def __init__(self, amount, fromCurr, toCurr):
        self.amount = amount
        self.fromCurrency = fromCurr
        self.toCurrency = toCurr
        self.actualOutput = {'input': {}, 'output': {}}

    # Convert input currencies to output
    def startConversion(self):
        # Write inputs
        self.writeInput()

        for toCurr in self.toCurrency:
            query = self.prepareConversionQuery(self.fromCurrency[0], toCurr)
            self.sendQueryAndGetResult(query, toCurr)

    # Create query
    def prepareConversionQuery(self, fromCurr, toCurr):
        conversionQuery = "http://rate-exchange-1.appspot.com/currency?from=" + str(fromCurr) + "&to=" + \
                          str(toCurr) + "&q=" + str(self.amount)
        return conversionQuery

    # Send query and store results
    def sendQueryAndGetResult(self, query, toCurr):
        conversionResult = urllib2.urlopen(query).read()
        self.writeOutput(toCurr, conversionResult)

    # Write actual input to dict
    def writeInput(self):
        self.actualOutput['input']['amount'] = self.amount
        self.actualOutput['input']['currency'] = self.fromCurrency[0]

    # Write actual output to dict
    def writeOutput(self, toCurr, conversionResult):
        data = json.loads(conversionResult, 'utf-8')
        self.actualOutput['output'][str(toCurr)] = str(data['v'])

    # Print conversion result
    def getConversionResult(self):
        print(json.dumps(self.actualOutput, indent=4, sort_keys=True))
