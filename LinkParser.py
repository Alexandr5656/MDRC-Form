import json
import webbrowser
import time
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import json
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
def openLinks(sheetDict):
    f = open('data.json', )
    shipCosts = json.load(f)
    f.close()
    print(shipCosts)
    browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(browser)
    companyPrices = dict()
    for company in sheetDict.keys():
        count= 0
        for partlist in sheetDict[company]:
            subTotal = 0
            for part in partlist:
                print(partlist)
                subTotal+=(part.price*part.quantity)
                if part.link == part.link:
                    pass
                    #webbrowser.open_new_tab(part.link)
            if count < (len(sheetDict[company])-1):
                fileName = "./finished/-" + company + "-" + str(count) + ".pdf"
                addPrices(0, subTotal, fileName)
                count+=1
            else:
                #shippingValue = input("Enter " + company + " shipping: \n")
                print(company)
                shippingValue = shipCosts[company]["shipping"]
                totalValue = (subTotal+float(shippingValue))
                fileName = "./finished/-" + company + "-" + str(len(sheetDict[company]) - 1) + ".pdf"
                companyPrices[company] = {"price": totalValue, "shipping": shippingValue}
                addPrices(float(shippingValue), totalValue, fileName)


    #with open('data.json', 'w') as json_file:
    #    json.dump(companyPrices, json_file)


def addPrices(ship,total,file):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)




    can.drawString(500, 300, "$" + ("{:.2f}".format(round(ship, 2))))
    can.drawString(500, 280, "$" + ("{:.2f}".format(round(total, 2))))
    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(file, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(file.replace("finished","shipping"), "wb")
    output.write(outputStream)
    outputStream.close()
