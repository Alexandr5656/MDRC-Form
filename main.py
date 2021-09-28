import loadPurchaseSheet as lps
import PDF as pdfLoaded
def main(fileName):
    sheet = lps.loadSheet(fileName)
    sortSheets(sheet)
#Sheet sorting
def sortSheets(sheetDict):
    for team in sheetDict:
        for company in sheetDict[team]:
            pdfLoaded.createPdfs(sheetDict)


main("test.xlsx")