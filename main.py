import loadPurchaseSheet as lps

def main(fileName):
    sheet = lps.loadSheet(fileName)
    sortSheets(sheet)
#Sheet sorting
def sortSheets(sheetDict):

    for team in sheetDict:
        print(team)

main("test.xlsx")