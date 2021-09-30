import loadPurchaseSheet as lps
import PDF as pdfLoaded
import LinkParser as linkP
def main(fileName):
    sheet = lps.loadSheet(fileName)
    sortSheets(sheet)
#Sheet sorting
def sortSheets(sheetDict):
    pdfLoaded.createPdfs(sheetDict)
    #linkP.parseLinkSheet(sheetDict)


main("test.xlsx")