from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import json
import math
f = open('Stores.json')
Stores = json.load(f)
f.close()

def projectHeader(can, name, team):
    can.drawString(125, 650, name)
    can.drawString(400, 650, team)


def vendor(can, company):
    newCompany = company.replace(" ","")
    if newCompany.lower() == "mcmaster" or newCompany.lower() == "mcmaster-carr":
        newCompany = "McMaster"
    can.drawString(217, 605, Stores[newCompany]["name"])
    can.drawString(217, 575, Stores[newCompany]["address"])
    can.drawString(217, 550, Stores[newCompany]["location"])
    can.drawString(217, 535, Stores[newCompany]["number"])
    can.drawString(217, 520, Stores[newCompany]["fax"])
    can.drawString(217, 505, Stores[newCompany]["email"])


def add_Item(can, amount, partNum, partName, unitPrice, lineNum):
    lineNum %= 5
    #42
    can.drawString(65, 460 - (lineNum * 29), str(int(amount)))
    can.drawString(92, 460 - (lineNum * 29), partNum)
    can.drawString(450, 460 - (lineNum * 29), "$" + str(unitPrice))

    can.drawString(500, 460 - (lineNum * 29), "$" + str(round(amount * unitPrice,2)))

    if len(partName)>42:
        wordIndex = 0
        letterIndex = 0
        words = partName.split(" ")
        for word in words:
            letterIndex += len(word)
            if letterIndex >42:
                letterIndex-=len(word)
                break
            letterIndex+=1
        can.setFontSize(10)
        can.drawString(175, 460 - (lineNum * 28)+5, partName[0:letterIndex-1])
        can.drawString(175, 460 - (lineNum * 28)-10, partName[letterIndex:len(partName)])
    else:
        can.drawString(175, 460 - (lineNum * 28), partName)
    return amount * unitPrice


def createPdf(parts, company,count):
    # Create Page
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    projectHeader(can, "MDRC", "")

    # Vendor Input
    vendor(can, company)

    # Part Purchase
    subTotal = 0.0
    for i in range(len(parts)):
        subTotal += add_Item(can,parts[i].quantity, "", parts[i].part, parts[i].price, i)


    can.drawString(500, 323, "$" + str(subTotal))
    # Name Line
    can.drawString(300, 243, "Alex Burbano arb8590@rit.edu")
    can.drawString(530, 243, "9/20/21")
    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("Form.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("./finished/"+"-"+ company+"-"+str(count) + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()


def createPdfs(partDictionary):
    for company in partDictionary:
        for i in range(len(partDictionary[company])):
            createPdf(partDictionary[company][i], company,i)