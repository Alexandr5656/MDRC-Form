import json
import webbrowser
import time
def parseLinkSheet(sheetDict):
    linkDict = dict()
    for company in sheetDict.keys():
        linkDict[company]=[]
        for partList in sheetDict[company]:
            linkArray = []
            for part in partList:
                linkArray.append(part.link)
            linkDict[company].append(linkArray)

    a_file = open("data.json", "w")
    json.dump(linkDict, a_file)
    openLinks(linkDict)
    openLinks(linkDict)
def openLinks(linkDict):
    browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(browser)
    for company in linkDict.keys():
        for partlist in linkDict[company]:
            for link in partlist:
                print(link)
                webbrowser.open_new_tab(link)
        shippingValue = input("Enter "+company+" shipping: \n")
        totalValue = input("Enter " + company + " shipping: \n")
        print(f'You entered {shippingValue} and {totalValue}')
