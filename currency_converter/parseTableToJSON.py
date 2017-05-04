from bs4 import BeautifulSoup

# Function parse HTML table and store data in dictionary
def parseTable():
    html_data = open("table.html", "r")

    table_data = [[cell.text for cell in row("td")]
                  for row in BeautifulSoup(html_data, "html.parser")("tr")]

    myDictionary = {}

    # Fill dictionary
    for row in table_data:
        myDictionary[row[1]] = row[4]

    html_data.close()
    return myDictionary
