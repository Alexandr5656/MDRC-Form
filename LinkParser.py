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
        fileName = "finished/-"+company+"-"+len(partlist)+".pdf"
        addPrices(shippingValue,totalValue,fileName)

def addPrices(ship,total,file):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)




    can.drawString(500, 300, "$" + str(ship))
    can.drawString(500, 280, "$" + str(total))
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
    outputStream = open(file, "wb")
    output.write(outputStream)
    outputStream.close()
